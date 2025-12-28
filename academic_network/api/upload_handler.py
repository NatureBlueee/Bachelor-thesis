"""
PDF Upload Handler
Handles file upload, calls DataLab API for conversion, moves files to appropriate directories
"""
import asyncio
import subprocess
from pathlib import Path
from typing import Dict, Any
import shutil

class UploadHandler:
    def __init__(self):
        # Find project root directory
        self.project_root = self._find_project_root()
        self.upload_dir = self.project_root / "Reference" / "PDF-MD" / "pdfs"
        self.output_dir = self.project_root / "Reference" / "PDF-MD" / "output_api"
        self.done_dir = self.project_root / "Reference" / "PDF-MD" / "pdfs_done"
        self.uncited_dir = self.project_root / "Reference" / "Uncited"

        # Ensure directories exist
        for dir_path in [self.upload_dir, self.output_dir, self.done_dir, self.uncited_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

    def _find_project_root(self) -> Path:
        """Find project root directory by locating MEMORY.md"""
        current = Path(__file__).parent.parent.parent
        for _ in range(5):
            if (current / "MEMORY.md").exists():
                return current
            current = current.parent
        return Path.cwd()

    async def handle_upload(self, filename: str, file_content: bytes) -> Dict[str, Any]:
        """
        Handle PDF upload

        Flow:
        1. Validate file type
        2. Save to pdfs/
        3. Start background conversion task
        4. Return task_id
        """
        # 1. Validate
        if not filename.endswith('.pdf'):
            return {"success": False, "error": "Only PDF files are supported"}

        # 2. Save file
        file_path = self.upload_dir / filename
        with open(file_path, 'wb') as f:
            f.write(file_content)

        # 3. Generate task_id
        task_id = f"upload_{filename}_{asyncio.get_event_loop().time()}"

        # 4. Start background conversion task
        asyncio.create_task(self._convert_and_move(file_path, task_id))

        return {
            "success": True,
            "task_id": task_id,
            "filename": filename,
            "status": "queued",
            "message": "PDF uploaded successfully, converting to Markdown..."
        }

    async def _convert_and_move(self, pdf_path: Path, task_id: str):
        """Background conversion task"""
        try:
            print(f"[{task_id}] Starting conversion: {pdf_path.name}...")

            # Call convert_api.py
            convert_script = self.project_root / "Reference" / "PDF-MD" / "convert_api.py"

            result = subprocess.run(
                ["python", str(convert_script)],
                cwd=str(convert_script.parent),
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes timeout
            )

            if result.returncode == 0:
                # Conversion successful, move files
                md_file = self.output_dir / f"{pdf_path.stem}.md"

                if md_file.exists():
                    # Move MD to Uncited/
                    target_md = self.uncited_dir / md_file.name
                    shutil.move(str(md_file), str(target_md))

                    # Move PDF to pdfs_done/
                    target_pdf = self.done_dir / pdf_path.name
                    shutil.move(str(pdf_path), str(target_pdf))

                    print(f"[{task_id}] OK Conversion successful: {md_file.name} -> Uncited/")
                else:
                    print(f"[{task_id}] WARNING Conversion completed but output file not found")
            else:
                print(f"[{task_id}] ERROR Conversion failed: {result.stderr}")

        except subprocess.TimeoutExpired:
            print(f"[{task_id}] ERROR Conversion timeout (5 minutes)")
        except Exception as e:
            print(f"[{task_id}] ERROR Conversion exception: {e}")


# Global instance
upload_handler = UploadHandler()

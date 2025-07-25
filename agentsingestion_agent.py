from utils.file_parser import parse_file
import uuid

class IngestionAgent:
    def __init__(self):
        self.name = "IngestionAgent"

    def ingest(self, file_path):
        trace_id = str(uuid.uuid4())  # Unique ID to trace the message
        extracted_text = parse_file(file_path)

        message = {
            "sender": self.name,
            "receiver": "RetrievalAgent",
            "type": "DOC_INGESTED",
            "trace_id": trace_id,
            "payload": {
                "text": extracted_text,
                "filename": file_path
            }
        }
        return message

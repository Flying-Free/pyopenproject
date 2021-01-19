import json

import model.attachment as att
from api_connection.exceptions.request_exception import RequestError
from api_connection.requests.post_request import PostRequest
from business.exception.business_error import BusinessError
from business.services.impl.command.attachment.attachment_command import AttachmentCommand


class Create(AttachmentCommand):

    def __init__(self, connection, filename, description, file_path):
        super().__init__(connection)
        self.filename = filename
        self.description = description
        with open(file_path, 'rb') as f:
            self.file_content = f.read()

    def execute(self):
        try:
            # TODO: Clients can create attachments without a container first and attach them later on.
            #  This is useful if the container does not exist at the time the attachment is uploaded.
            #  After the upload, the client can then claim such containerless attachments for any resource eligible
            #  (e.g. WorkPackage) on subsequent requests.
            #  The upload and the claiming must be done for the same user account.
            #  Attachments uploaded by another user cannot be claimed and once claimed for a resource,
            #  they cannot be claimed by another.
            #  The upload request must be of type multipart/form-data with exactly two parts.
            #  The first part must be called metadata. Its content type is expected to be application/json,
            #  the body must be a single JSON object, containing at least the fileName and optionally
            #  the attachments description.
            #  The second part must be called file, its content type should match the mime type of the file.
            #  The body must be the raw content of the file.
            #  Note that a filename must be indicated in the Content-Disposition of this part,
            #  although it will be ignored.
            #  Instead the fileName inside the JSON of the metadata part will be used.
            metadata = {"fileName": self.filename, "description": {"raw": self.description}}
            json_obj = PostRequest(connection=self.connection,
                                   context=f"{self.CONTEXT}",
                                   files={'file': ('attachment', self.file_content),
                                          'metadata': (None, json.dumps(metadata))
                                          }).execute()
            return att.Attachment(json_obj)
        except RequestError as re:
            raise BusinessError(f"Error creating attachment : {self.filename}") from re

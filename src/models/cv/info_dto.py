from mongoengine import ListField, Document, StringField

class CVInfo(Document):
    organization= ListField(required=False)
    major= ListField(required=False)
    gpa= ListField(required=False)
    name= ListField(required=False)
    skill= ListField(required=False)
    gender= ListField(required=False)
    job_title= ListField(required=False)
    profile_url= ListField(required=False)
    email= ListField(required=False)
    phone= ListField(required=False)
    education=ListField(required=False)
    batch_id=StringField(required=False)
    file_path=StringField(required=False)
    image_paths=ListField(required=False)

    def to_document(self):
        return self.__dict__

class BatchCVInfo(Document):
    cv_ids = ListField(required=False)
    def to_document(self):
        return self.__dict__

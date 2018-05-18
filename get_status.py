import cognitive_face as CF
from global_variables import personGroupId

Key = '63fdb1a3135b4d71bf3b9866173e8ea7'

CF.Key.set(Key)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)


res = CF.person_group.get_status(personGroupId)
print res

#!python
# coding=utf-8

# @Author              : Uncle Bean
# @Date                : 2020-03-23 09:42:56
# @LastEditors: Uncle Bean
# @LastEditTime: 2020-03-23 13:05:31
# @FilePath            : \src\utils\img\ocr.py
# @Description         : 

import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


class OCR(object):

    def img_to_excel(self, 
            image_path, 
            secret_id, 
            secret_key):

        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        cred = credential.Credential(
            secret_id, 
            secret_key
            )

        # 实例化client对象
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        clientProfile.signMethod = "TC3-HMAC-SHA256"
        client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

        # 实例化一个请求对象
        req = models.GeneralFastOCRRequest()
        
        # 读取图片数据，使用Base64编码
        with open(image_path, 'rb') as f:
            image = f.read()
            image_base64 = str(base64.b64encode(image), encoding='utf-8')
        req.ImageBase64 = image_base64

        # 通过client对象调用访问接口，传入请求对象
        resp = client.TableOCR(req)

        # 获取返回数据（Data为Base64编码后的Excel数据）
        data = resp.Data

        # 转换为Excel
        path_excel = image_path + ".xlsx"
        with open(path_excel, 'wb') as f:
            f.write(base64.b64decode(data))
        return path_excel

    
if __name__ == "__main__":
    image = r'C:\Temp\test.png'
    ocr = OCR()
    ocr.img_to_excel(image)
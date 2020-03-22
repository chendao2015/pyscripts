import requests
import json
import re
import os, shutil
import urllib.request, urllib.error
from Crypto.Cipher import AES
import sys


def aes_decode(data, key):
    """AES解密
    :param key:  密钥（16.32）一般16的倍数
    :param data:  要解密的数据
    :return:  处理好的数据
    """
    cryptor = AES.new(key, AES.MODE_CBC, key)
    plain_text = cryptor.decrypt(data)
    return plain_text.rstrip(b'\0')


def getUrlData(url, DOWNLOAD_PATH):
    """打开并读取网页内容index.m3u8
    :param url: 包含ts文件流的m3u8连接
    :return:  包含TS链接的文件
    """
    try:
        urlData = urllib.request.urlopen(url, timeout=20)  # .read().decode('utf-8', 'ignore')
        return urlData
    except Exception as err:
        error_log = os.path.join(DOWNLOAD_PATH, 'error.log')
        with open(error_log, 'a+') as f:
            f.write('下载出错 (%s)\n' % url, err, "\n")
        print('下载出错 (%s)\n' % url, err)
        return -1


def getDown_reqursts(url, file_path, key):
    """  下载ts视频流
    :param url: ts流链接
    :param file_path: 临时文件路径
    :param key: 加密密钥
    """
    try:
        response = requests.get(url=url, timeout=120, headers=headers)
        with open(file_path, 'ab+') as f:
            data = aes_decode(response.content, key)
            f.write(data)
    except Exception as e:
        print(e)


def getVideo_requests(url_m3u8, video_Name, key, DOWNLOAD_PATH):
    """ 根据m3u8文件提取出
    :param url_m3u8: 包含ts文件流的m3u8连接
    :param video_Name: 下载的视频名称地址
    :param key: 加密密钥
    """
    print('>>> 开始下载 ！ \n')
    urlData = getUrlData(url_m3u8, DOWNLOAD_PATH)
    tempName_video = os.path.join(DOWNLOAD_PATH, '%s.ts' % video_Name)  # 创建临时文件
    open(tempName_video, "wb").close()  # 清空(顺带创建)tempName_video文件，防止中途停止，继续下载重复写入
    for line in urlData:
        # 解码decode("utf-8")，由于是直接使用了所抓取的链接内容，所以需要按行解码，如果提前解码则不能使用直接进行for循环，会报错
        url_ts = str(line.decode("utf-8")).strip()  # 重要：strip()，用来清除字符串前后存在的空格符和换行符
        if not '.ts' in url_ts:
            continue
        else:
            if not url_ts.startswith('http'):  # 判断字符串是否以'http'开头，如果不是则说明url链接不完整，需要拼接
                # 拼接ts流视频的url
                url_ts = url_m3u8.replace(url_m3u8.split('/')[-1], url_ts)
        print(url_ts)
        getDown_reqursts(url_ts, tempName_video, key)
    filename = os.path.join(DOWNLOAD_PATH, '%s.mp4' % video_Name)
    shutil.move(tempName_video, filename)  # 转成MP4文件
    print('>>> %s.mp4 下载完成! ' % video_Name)


if __name__ == '__main__':
    '''
    https://play2.172cat.com/202003/21/xUiOhNCD/500kb/hls/index.m3u8    
    '''
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    baseurl = 'https://play2.172cat.com/202003/21/xUiOhNCD/500kb/hls/index.m3u8'

    key = requests.get('https://play2.172cat.com/202003/21/xUiOhNCD/500kb/hls/key.key').content
    getVideo_requests(baseurl,'2',key,'video/')
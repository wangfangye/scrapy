import math
import requests
import re
headers = {
    'Host':'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Cookie':'_xsrf=OZuTmQz4ADpPq3Pajb95MHgb8nLk6yc9; _zap=45654567-0b46-497a-8e3c-be1fe6fc3592; d_c0="ADDlXQWjBA6PTgntw_w6U1u4fCOmqkh4vHE=|1533609338"; q_c1=3179e2ea098641b48c6e15c4ebdb72a4|1533609632000|1533609632000; l_cap_id="YjAxZGIxOWEzNTFiNGE4Mjk0YTZiN2E0OTA5OWViNTY=|1533638246|a3526dd07543b76d7b2d5985871ec7c7b8282302"; r_cap_id="YmQ4YjZlNjQzMDMyNGI2YmJmYjc5NjNmN2EyZmU4ZjU=|1533638246|f1063645c320a3818a9bbbf5ba49977cb14957a9"; cap_id="MGU0NTQ0ZGNlZDM4NDcxYjliMzRmNDJkZmI5Zjg2NDc=|1533638246|87fff2f218a784c9253859c491ce7e6f3f51fcc6"; __utma=51854390.85065723.1533638250.1533638250.1533638250.1; __utmz=51854390.1533638250.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20180807=1; capsion_ticket="2|1:0|10:1533961894|14:capsion_ticket|44:OGIzODIwN2E4ZGY4NDc4M2FkNjY2YTg5MzczOGYwYzQ=|4f782072378b6db54359a21d83df2c881f225a2e6e12fbbe6bbed24bbb3f9a24"; z_c0="2|1:0|10:1533961912|4:z_c0|92:Mi4xblFLMUFBQUFBQUFBTU9WZEJhTUVEaVlBQUFCZ0FsVk51TFJiWEFDYkFRZEVYMmNhZzJxOGtZZXBEVUtYUDFDSTdB|532a3b4c3a655e4069be49ca4f4858c2d4f7578646ef99cf7b1de946f9ebcf08"; tgw_l7_route=3072ae0b421aa02514eac064fb2d64b5'
}

res = requests.get('https://www.zhihu.com',headers = headers)
print(res.status_code)


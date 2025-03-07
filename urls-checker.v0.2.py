import requests
import time

# 配置参数
url = "https://example.com"  # 测试网页地址
check_interval = 60  # 发包测试间隔(s)
retry_times = 5      # 无响应重试次数
retry_interval = 5   # 无响应重试间隔(s)

def check_url(url):
    """检查网页是否返回200状态码"""
    try:
        r = requests.get(url)
        return r.status_code == 200
    except requests.RequestException:
        return False

def main():
    """主函数，执行网页检查逻辑"""
    start_time = time.time()
    print(f"Start checking {url} at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

    while True:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if check_url(url):
            print(f"{current_time} success")
            time.sleep(check_interval)
        else:
            print(f"{current_time} error, starting retries")
            for attempt in range(retry_times):
                time.sleep(retry_interval)
                retry_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                if check_url(url):
                    print(f"{retry_time} retry {attempt + 1} success")
                    break
                else:
                    print(f"{retry_time} retry {attempt + 1} failed")
            else:
                # 所有重试都失败
                end_time = time.time()
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} Failed after {retry_times} retries!")
                print(f"Total running time: {end_time - start_time:.2f} seconds")
                break

if __name__ == "__main__":
    main()
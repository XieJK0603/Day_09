from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素类"""

    """搜索页面元素"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")

    """设置页面"""
    # 更多
    setting_more_btn_xpath = (By.XPATH, "//*[contains(@text,'更多')]")

    """更多页面"""
    # 移动网络
    more_mobile_btn_xpath = (By.XPATH, "//*[contains(@text,'移动网络')]")

    """移动网络设置页面"""
    # 首选网络类型
    mobile_one_network_xpath = (By.XPATH, "//*[contains(@text,'首选网络')]")
    # 2G
    mobile_select_2G_btn_xpath = (By.XPATH, "//*[contains(@text,'2G')]")
    # 获取当前页面所有summary信息
    mobile_get_summary_text_ids = (By.ID, "android:id/summary")

from selenium.webdriver.common.by import By

from Base.base import Base


class SearchPage:

    def __init__(self, driver):
        # 实例化Base类
        self.base_obj = Base(driver)
        """搜索页面元素"""
        # 搜索按钮
        self.search_btn = (By.ID, "com.android.settings:id/search")
        # 输入框
        self.search_input = (By.ID, "android:id/search_src_text")
        # 搜索结果
        self.search_result = (By.ID, "com.android.settings:id/title")

    def click_search_btn(self):
        """点击搜索按钮"""
        self.base_obj.click_ele(self.search_btn)

    def search_text(self, text):
        """
        搜索内容
        :param text: 输入文本内容
        :return:
        """
        self.base_obj.send_ele(self.search_input, text)

    def ge_search_result(self):
        """
        获取搜索结果
        :return: 列表
        """
        # 定位
        results = self.base_obj.search_eles(self.search_result)
        # 返回
        return [i.text for i in results]

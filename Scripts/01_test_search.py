from appium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Base.base import Base


class TestPep:

    def setup_class(self):
        """初始化driver"""
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app的信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 声明我们的driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 实例化driver对象
        self.base_obj = Base(self.driver)
        """元素"""
        # 搜索按钮
        self.search_btn = (By.ID, "com.android.settings:id/search")
        # 输入框
        self.search_input = (By.ID, "android:id/search_src_text")
        # 搜索结果
        self.search_result = (By.ID, "com.android.settings:id/title")

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_search(self):
        """进入搜索页面 -class"""
        # 点击搜索
        self.base_obj.click_ele(self.search_btn)

    @pytest.mark.parametrize("search_data,exp_data", [("1", "休眠"), ("m", "MAC地址"), ("w", "WPS按钮")])
    def test_search(self, search_data, exp_data):
        """
        测试方法
        :param search_data: 搜索内容
        :param exp_data: 预期包含结果
        :return:
        """
        print("\n搜索内容:{},预期结果:{}".format(search_data, exp_data))
        # 输入搜索内容
        self.base_obj.send_ele(self.search_input, search_data)
        # 获取结果列表
        results = self.base_obj.search_eles(self.search_result)
        # 断言
        assert exp_data in [i.text for i in results]


if __name__ == '__main__':
    pytest.main(["01_test_search.py"])

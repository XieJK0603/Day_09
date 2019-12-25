import pytest
import sys, os

sys.path.append(os.getcwd())  # 添加自动移路径到python搜索路径

from Page.searchPage import SearchPage
from Base.getDriver import get_android_driver


class TestPep:

    def setup_class(self):
        # 声明我们的driver对象
        self.driver = get_android_driver('com.android.settings', '.Settings')
        # 实例化页面类对象
        self.search_obj = SearchPage(self.driver)

    def teardown_class(self):
        """退出driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_search(self):
        """进入搜索页面 -class"""
        # 点击搜索
        self.search_obj.click_search_btn()

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
        self.search_obj.search_text(search_data)
        # 断言
        assert exp_data in self.search_obj.ge_search_result()
#
#
if __name__ == '__main__':
    pytest.main(["01_test_search.py"])

import pytest, sys, os

sys.path.append(os.getcwd())

from Base.page import Page

from Base.getDriver import get_android_driver


class TestSetNetwork:

    def setup_class(self):
        """初始化driver"""
        # driver
        self.driver = get_android_driver('com.android.settings', '.Settings')
        # 实例化统一入口类
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        """结束driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_set_network_page(self):
        """进入修改网络页面"""
        # 点击更多
        self.page_obj.get_setting_page().click_more_btn()
        # 点击移动网络
        self.page_obj.get_more_page().click_mobile_btn()

    def test_set_network(self):
        """修改手机网络"""
        # 选择网络
        self.page_obj.get_mobile_page().select_network()
        # 断言
        assert "2G" in self.page_obj.get_mobile_page().get_summary_list()

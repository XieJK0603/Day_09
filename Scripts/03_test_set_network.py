import pytest, sys, os

sys.path.append(os.getcwd())

from Page.settingPage import SettingPage
from Page.morePage import MorePage
from Page.mobilePage import MobilePage

from Base.getDriver import get_android_driver


class TestSetNetwork:

    def setup_class(self):
        """初始化driver"""
        # driver
        self.driver = get_android_driver('com.android.settings', '.Settings')
        # 实例化设置页面类
        self.setting_obj = SettingPage(self.driver)
        # 实例化更多页面类
        self.more_obj = MorePage(self.driver)
        # 实例化移动网络页面类
        self.mobile_obj = MobilePage(self.driver)


    def teardown_class(self):
        """结束driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_set_network_page(self):
        """进入修改网络页面"""
        # 点击更多
        self.setting_obj.click_more_btn()
        # 点击移动网络
        self.more_obj.click_mobile_btn()

    def test_set_network(self):
        """修改手机网络"""
        # 选择网络
        self.mobile_obj.select_network()
        # 断言
        assert "2G" in self.mobile_obj.get_summary_list()

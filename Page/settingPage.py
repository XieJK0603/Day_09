from Base.base import Base
from Page.pageElements import PageElements


class SettingPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_more_btn(self):
        """点击设置页面更多按钮"""
        self.click_ele(PageElements.setting_more_btn_xpath)

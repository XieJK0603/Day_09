from Base.base import Base
from Page.pageElements import PageElements


class MobilePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def select_network(self):
        """选择2G网络"""

        # 点击首选网络类型
        self.click_ele(PageElements.mobile_one_network_xpath)
        # 选择2G网络
        self.click_ele(PageElements.mobile_select_2G_btn_xpath)

    def get_summary_list(self):
        """返回所有summary列表"""
        # 定位一组元素
        results = self.search_eles(PageElements.mobile_get_summary_text_ids)
        # 返回文本列表
        return [i.text for i in results]

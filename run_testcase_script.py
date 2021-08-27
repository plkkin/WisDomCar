import time
import unittest
from unittest import runner

import HTMLTestRunnerCN

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 生成的报告路径
    filePath = './report/' + now + 'report.html'
    fp = open(filePath, 'wb')

    # 生成的报告title描述
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title="智慧警车系统自动化测试报告",
        description='详细测试用例结果',
        tester='秦德宪'
    )
    # 运行测试用例 Wis_Dom_Car_*.py
    discover = unittest.defaultTestLoader.discover('./testcase', pattern='Wis_Dom_Car_*.py')
    runner.run(discover)
    # 关闭文件
    fp.close()

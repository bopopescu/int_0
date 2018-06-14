#!/user/bin/env python
#_*_ coding:utf-8 _*_
from runmethod import RunMethod
from get_data import GetData
from common_util import CommonUtil
from data.depend_data import DependdentData
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com = CommonUtil()
    #程序执行的入口
    def go_on_run(self):
        res = None
        rows_count = int(self.data.get_case_lines())
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_way(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expect_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    #响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method, url, request_data, header)
                #print res
                if self.com.is_contain(expect,res):
                    # self.data.write_result(i,'pass')
                    print 'pass'
                else:
                    # self.data.write_result(i, 'fail')
                    print 'fail'
if __name__ == "__main__":
    run = RunTest()
    run.go_on_run()








# conding = utf-8
import time
import threading
# import sys  # 需要单独使用的时候，加上这个全局路径申明
#
# sys.path.append('~/PycharmProjects/Automator_for_Appium_python/Code_PO')
from utils.dos_cmd import DOScmd
from utils.port import Port
from utils.write_user_command import WriteUserCommand


class Server:
    def __init__(self):
        self.cmd = DOScmd()
        self.port = Port()
        self.write_file = WriteUserCommand()
        self.device_list = self.get_devices()

    def get_devices(self):
        # """
        # 	通过adb devices命令查询当前PC所连接的设备数量，并将查询的设备信息储存为一个list
        # """
        devices_list = []
        result_list = self.cmd.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
        else:
            print("找不到已连接设备")
            devices_list = None

        return devices_list

    def create_command_list(self, i, start_port, start_bootstrap_port):
        # """
        # 	拼接生成Appium的启动命令
        # 	start_port：-p后接的起始端口值
        # 	start_bootstrap_port：-bp后接的起始端口值
        # """
        command_list = []
        if self.device_list != None:
            t = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
            port_list = self.port.create_port_list(start_port, self.device_list)
            # print(port_list)
            bootstrap_port_list = self.port.create_port_list(start_bootstrap_port, self.device_list)
            # 拼接Appium启动命令
            command = "appium -p {} -bp {} -U {} --no-reset --session-override --log ../log/{}_log_{}".format(
                port_list[i], bootstrap_port_list[i], self.device_list[i], self.device_list[i], t)
            command_list.append(command)
            self.write_file.Write_data(i, self.device_list[i], port_list[i], bootstrap_port_list[i])
            print(command_list)
            return command_list
        else:
            print('生成Appium启动命令失败')
            return None

    def start_server(self, i):
        # 封装一个启动Appium的方法
        start_list = self.create_command_list(i, 4700, 4900)
        self.cmd.excute_cmd(start_list[0])

    def kill_server(self, process):
        # 封装一个杀掉Appium进程的方法
        server_list = self.cmd.excute_cmd_result('tasklist | find "{}"'.format(process))
        # print(server_list)
        if len(server_list) > 0:
            self.cmd.excute_cmd("taskkill -F -PID {}".format(process))

    def main(self):
        self.kill_server('node.exe')  # 清除进程
        self.write_file.clear_data()  # 清除历史数据
        for i in range(len(self.device_list)):
            # 通过多线程方法，同时启动多个Appium
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()
        time.sleep(20)


if __name__ == '__main__':
    Server().main()
    # print(Server().get_devices())


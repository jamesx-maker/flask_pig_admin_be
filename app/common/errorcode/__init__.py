# coding: utf8
'定义错误码'

error_code = {
    # `app/back/controller/piginfo`
    '1000_0001': '1000_0001: 向数据库插入数据失败',
    # `app/back/controller/stationinfo`
    '1000_1001': '1000_1001: 向数据库插入数据失败',
    # `app/back/controller/phonemessage`
    '1000_2001': '1000_2001: 短信发送失败',
    # `app/common/util/send_mail/__init__`
    '1000_3001': '1000_3001: 邮件发送失败',
    # `app/admin/controller/notificationcontact`
    '1000_4001': '1000_4001: 通知邮箱添加失败',
    # `app/admin/controller/stationinfo`
    '1000_5001': '1000_5001: 获取测定站信息失败',
    '1000_5002': '1000_5002: 添加测定站失败，请检查测定站是否已经存在',
    '1000_5003': '1000_5003: 删除测定站失败',
    '1000_5004': '1000_5004: 更新测定站信息失败',
    # `app/admin/controller/piginfo`
    '1000_6001': '1000_6001: 获取种猪信息失败',
    # `app/admin/controller/piginfo`
    '1000_6101': '1000_6101: 导出种猪信息失败，具体原因请查看日志',
    '1000_6102': '1000_6102: 导出种猪信息失败',
    # `app/admin/controller/errorcode`
    '1000_7001': '1000_7001: 查询故障码失败',
    '1000_7101': '1000_7101: 删除故障码失败',
    '1000_7201': '1000_7201: 添加故障码失败',
    '1000_7301': '1000_7301: 更改故障码失败',

    # `app/admin/controller/syscfg
    '1000_8001': '1000_8001: 获取系统全部配置失败',
    '1000_8002': '1000_8002: 更改系统部分配置失败',

    # `app/admin/controller/login
    '1000_9001': '1000_9001: 注册失败',
    '1000_9002': '1000_9002: 登录失败',
    '1000_9003': '1000_9003: 重置密码失败',
    '1000_9004': '1000_9004: 激活密码失败',

    # `app/admin/controller/piglist
    '1001_0001': '1001_0001: 获取测定站内的所有种猪失败',
    '1001_0002': '1001_0002: 种猪入栏失败',
    '1001_0003': '1001_0003: 单头猪出栏失败',
    '1001_0004': '1001_0004: 一栏猪出栏失败',
    '1001_0005': '1001_0005: 更改种猪信息失败',

    # `app/admin/controller/pigbase
    '1002_0001': '1002_0001: 种猪基础信息插入失败',
    '1002_0002': '1002_0002: 种猪日采食信息处理失败',
    '1002_0003': '1002_0003: 查询种猪基础信息失败',

    # `app/admin/controller/station_weekly_assessment
    '1003_0001': '1003_0001: 测定站周采食量统计数据处理失败',

    # `app/admin/controller/pig_intake
    '1004_0001': '1004_0001: 个体采食量趋势数据处理失败',
    '1004_0002': '1004_0002: 测定站某日每头猪的采食总量数据处理失败',

    # `app/admin/controller/graphanalyse
    '1005_0001': '1005_0001: 采食量区间数据处理失败',
    '1005_0002': '1005_0002: 体重变化数据处理失败',


    # `app/common/memory/stationinfo`
    '1100_0001': '1100_0001: 测定站号列表存入内存失败',
    # `app/common/memory/facnum`
    '1100_1002': '1100_1002: 猪场代码存入内存失败',
    '1100_2003': '1100_2003: 猪场代码比对失败',
    # `app/common/memory/piglistfacnum`
    '1100_2001': '1100_2001: 种猪列表信息代码存入内存失败',
    # `app/common/memory/daily_intake_start_time`
    '1100_3001': '1100_3001: 种猪日采食开始时间存入内存失败',
    '1100_3002': '1100_3002: 检查输入的时间是否在指定的开始时间之后失败',
    # `app/common/memory/daily_first_intake_record`
    '1100_4001': '1100_4001: 日首次采食数据载入内存失败',
    '1100_4002': '1100_4002: 查询种猪今日首次采食数据是否存在失败',
    # `app/common/memory/pig_daily_assess_record`
    '1100_5001': '1100_5001: 种猪最近两日采食、体重数据载入内存失败',
    '1100_5002': '1100_5002: has_today_intake 该种猪今天是否已经采食调用失败',
    '1100_5003': '1100_5003: 添加种猪当日采食记录失败',
    '1100_5004': '1100_5004: 更改种猪当日采食记录失败',
    '1100_5005': '1100_5005: 计算当日采食数据失败',
}

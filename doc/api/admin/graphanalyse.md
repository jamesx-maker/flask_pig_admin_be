# admin/graphanalyse

### `GET` /admin/graphanalyse/food_intake_interval_analysis/

采食量区间分析

__params__

- `type` `string` `required` 是选择的一个测定站还是所有的测定站 `all` `one`
- `stationId` `string` 测定站 id
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "count": 443, // 这段是时间的总的记录数
        "data": [
            {
                "count": 267, // 采食量在 [0, 200) 之间的数量
                "frequency": 0.6, // 频率
                "intake": "0-200" // 采食量区间
            },
            {
                "count": 132,
                "frequency": 0.3,
                "intake": "200-400"
            },
            {
                "count": 38,
                "frequency": 0.09,
                "intake": "400-600"
            },
            {
                "count": 4,
                "frequency": 0.01,
                "intake": "600-800"
            },
            {
                "count": 2,
                "frequency": 0,
                "intake": "800-1000"
            },
            {
                "count": 0,
                "frequency": 0,
                "intake": "1000-1200"
            },
            {
                "count": 0,
                "frequency": 0,
                "intake": "1200-1400"
            },
            {
                "count": 0,
                "frequency": 0,
                "intake": "1400-1600"
            },
            {
                "count": 0,
                "frequency": 0,
                "intake": ">1600"
            },
        ]
    },
}
```

### `GET` /admin/graphanalyse/weight_change/

体重变化趋势图

__params__
- `type` `string` `required` 是显示一个测定站的数据还是显示一头猪的数据 `station` 查询一个测定站的所有猪的体重变化，`pig` 一头猪的体重变化
- `stationId` `string` `required` 测定站 id，`type=station` 时
- `pid` `string` `required` 种猪 id，`type=pig` 时
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    // 数组的在当天有值，没有数据的则没有该耳标号和值
    data: {
        "data": [
            {
                "000009000401": 44.02,
                "000009000402": 40.4,
                "000009000406": 48.46,
                "000009000407": 50.37,
                "000009000409": 49.87,
                "000009000413": 48.96,
                "000009000420": 46.03,
                "000009000421": 47.05,
                "000009000425": 42.62,
                "000009000426": 30.15,
                "000009000427": 43.7,
                "000009000436": 28.15,
                "000009000448": 49.9,
                "000009000449": 38.11,
                "date": "03-20"
            },
            {
                "000009000401": 44.52,
                "000009000402": 40.8,
                "000009000406": 48.2,
                "000009000407": 50.73,
                "000009000409": 46.43,
                "000009000413": 50.02,
                "000009000420": 46.24,
                "000009000421": 48.2,
                "000009000425": 42.24,
                "000009000427": 43.62,
                "000009000448": 49.64,
                "000009000449": 38.37,
                "date": "03-21"
            },
            {
                "000009000401": 45.05,
                "000009000402": 41.78,
                "000009000406": 47.9,
                "000009000407": 51.31,
                "000009000409": 44.8,
                "000009000413": 51.17,
                "000009000420": 46.97,
                "000009000421": 49.55,
                "000009000425": 43.28,
                "000009000427": 43.49,
                "000009000448": 50.84,
                "000009000449": 39.79,
                "000009999009": 45.93,
                "date": "03-23"
            },
            {
                "000009000401": 45.41,
                "000009000402": 42.2,
                "000009000406": 48.06,
                "000009000407": 52.7,
                "000009000409": 48.19,
                "000009000413": 52.27,
                "000009000420": 47.69,
                "000009000421": 49.7,
                "000009000425": 44.02,
                "000009000427": 43.67,
                "000009000448": 51.24,
                "000009000449": 39.72,
                "date": "03-24"
            },
            {
                "000009000413": 50.42,
                "date": "03-22"
            }
        ],
        "earIdArr": [
            "000009000409",
            "000009000426",
            "000009000420",
            "000009000449",
            "000009000402",
            "000009999009",
            "000009000421",
            "000009000436",
            "000009000407",
            "000009000406",
            "000009000427",
            "000009000401",
            "000009000448",
            "000009000425",
            "000009000413"
        ]
    },
}
```

### `GET` /admin/graphanalyse/intake_frequency_in_day_interval/

不同时段采食频率分布图

__params__
- `type` `string` `required` 是选择的一个测定站还是所有的测定站 `all` `one`
- `stationId` `string` 测定站 id
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: {
        "count": 138, // 在该总的时间段内的所有的记录数
        "data": [
            {
                "count": 8, // 在 "00:00-02:00" 时间段内有记录的条数
                "frequency": 0.06, // 分布的频率
                "interval": "00:00-02:00" // 所属的时间段
            },
            {
                "count": 12,
                "frequency": 0.09,
                "interval": "02:00-04:00"
            },
            {
                "count": 10,
                "frequency": 0.07,
                "interval": "04:00-06:00"
            },
            {
                "count": 16,
                "frequency": 0.12,
                "interval": "06:00-08:00"
            },
            {
                "count": 21,
                "frequency": 0.15,
                "interval": "08:00-10:00"
            },
            {
                "count": 14,
                "frequency": 0.1,
                "interval": "10:00-12:00"
            },
            {
                "count": 15,
                "frequency": 0.11,
                "interval": "12:00-14:00"
            },
            {
                "count": 14,
                "frequency": 0.1,
                "interval": "14:00-16:00"
            },
            {
                "count": 12,
                "frequency": 0.09,
                "interval": "16:00-18:00"
            },
            {
                "count": 5,
                "frequency": 0.04,
                "interval": "18:00-20:00"
            },
            {
                "count": 8,
                "frequency": 0.06,
                "interval": "20:00-22:00"
            },
            {
                "count": 3,
                "frequency": 0.02,
                "interval": "22:00-24:00"
            }
        ]
    },
}
```


### `GET` /admin/graphanalyse/daily_weight_gain_and_fcr/

日增重和饲料转化率统计（FCR）

__params__
- `stationId` `string` `required` 测定站 id
- `startTime` `string` `required` 起始时间 10 位数字时间戳
- `endTime` `string` `required` 起始时间 10 位数字时间戳

__return__

```js
ret = {
    success: boolean,  // true || false
    err_msg: string, // 操作失败的时候，返回的错误信息
    data: [
        {
            "animalNum": "", // 种猪号
            "dailyWeightGain": 0.2, // 日增重
            "earId": "000009000402", // 耳标号
            "fcr": 0.2, // 饲料转化率
            "pid": 2 // 种猪 id
        },
        {
            "animalNum": "",
            "dailyWeightGain": -0.13,
            "earId": "000009000406",
            "fcr": -0.13,
            "pid": 3
        },
        {
            "animalNum": "",
            "dailyWeightGain": -0.04,
            "earId": "000009000427",
            "fcr": -0.04,
            "pid": 4
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0.13,
            "earId": "000009000449",
            "fcr": 0.13,
            "pid": 5
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0.105,
            "earId": "000009000420",
            "fcr": 0.11,
            "pid": 6
        },
        {
            "animalNum": "",
            "dailyWeightGain": -1.72,
            "earId": "000009000409",
            "fcr": -1.72,
            "pid": 7
        },
        {
            "animalNum": "",
            "dailyWeightGain": -0.19,
            "earId": "000009000425",
            "fcr": -0.19,
            "pid": 8
        },
        {
            "animalNum": "",
            "dailyWeightGain": -0.13,
            "earId": "000009000448",
            "fcr": -0.13,
            "pid": 9
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0.53,
            "earId": "000009000413",
            "fcr": 0.53,
            "pid": 10
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0.575,
            "earId": "000009000421",
            "fcr": 0.58,
            "pid": 11
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0.18,
            "earId": "000009000407",
            "fcr": 0.18,
            "pid": 12
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0,
            "earId": "000009000436",
            "fcr": 0,
            "pid": 13
        },
        {
            "animalNum": "",
            "dailyWeightGain": 0,
            "earId": "000009000426",
            "fcr": 0,
            "pid": 14
        }
    ],
}
```

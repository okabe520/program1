# Area Calculator

基于 Python tkinter 的图形面积计算器，支持正方形、长方形、三角形、圆形，可切换厘米/英寸单位。

## 运行

```bash
python main.py
```

## 测试

```bash
python -m unittest test.py
```

## 功能

- 四种形状：正方形 / 长方形 / 三角形 / 圆形
- 单位切换：cm / in（自动换算）
- GUI 界面 (tkinter)

## 架构

```
Shape (基类)
├── Square      # 正方形
├── Rectangle   # 长方形
├── Triangle    # 三角形
└── Circle      # 圆形
AreaCalculatorApp  # tkinter GUI
```

## 团队

- 黄云聪：代码主体框架、GUI、测试
- 王舒瑜：正方形和长方形类
- 许可：三角形和圆形类
- 朱永威：面积计算函数、帮助文档

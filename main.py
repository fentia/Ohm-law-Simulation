# 主程序

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox
import matplotlib.patches as patches

# 欢迎页
def show_main_page():
    for widget in root.winfo_children():
        widget.destroy()
    
    label = tk.Label(root, text="欢迎使用欧姆定律仿真教具", font=("微软雅黑", 50))
    label.pack(expand=True)
    
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    
    go_group_btn = tk.Button(btn_frame, text="确定", font=("微软雅黑", 12), command=show_group_page)
    go_group_btn.pack(side="left", padx=10)
    
    exit_btn = tk.Button(btn_frame, text="退出", font=("微软雅黑", 12), command=root.destroy)
    exit_btn.pack(side="left", padx=10)

# 小组介绍页
def show_group_page():
    for widget in root.winfo_children():
        widget.destroy()
    info_text = "By Fentia"
    label = tk.Label(root, text=info_text, font=("微软雅黑", 50), justify="center")
    label.pack(expand=True)
    
    # 按钮容器
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)
    
        
    open_sim_btn = tk.Button(btn_frame, text="开始使用", font=("微软雅黑", 12), command=open_matplotlib_simulation)
    open_sim_btn.pack(side="left", padx=10)

    back_btn = tk.Button(btn_frame, text="返回", font=("微软雅黑", 12), command=show_main_page)
    back_btn.pack(side="left", padx=10)

# 仿真程序
def open_matplotlib_simulation():
    # 设置中文字体支持
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun', 'KaiTi']
    plt.rcParams['axes.unicode_minus'] = False

    # 创建图形和坐标轴
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('欧姆定律仿真教具', fontsize=16, fontweight='bold', color='navy')

    # 初始电路参数
    power_voltage = 6.0
    fixed_resistor = 10.0
    slider_resistance = 5.0
    switch_closed = False

    def calculate_values():
        total_resistance = fixed_resistor + slider_resistance
        current = power_voltage / total_resistance if switch_closed else 0.0
        voltage = current * fixed_resistor
        return current, voltage

    current, voltage = calculate_values()

    def draw_components():
        ax.clear()
        ax.set_xlim(-1, 13)
        ax.set_ylim(-1, 8)
        ax.axis('off')
        ax.set_title('欧姆定律仿真教具', fontsize=16, fontweight='bold', color='navy')
        
        # 电源
        ax.add_patch(patches.Rectangle((0.5, 1.5), 0.5, 2.0, fill=True, color='lightgray', edgecolor='black'))
        ax.plot([0.75, 0.75], [3.0, 3.4], 'k-', lw=2)
        ax.plot([0.75, 0.75], [1.1, 1.5], 'k-', lw=2)
        ax.text(0.65, 2.5, '+', fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(0.65, 1.8, '-', fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(0.3, 2.5, '电源', fontsize=12, ha='right', va='center', color='darkred')
        
        # 开关
        switch_x, switch_y = 2.5, 2.5
        ax.plot([switch_x, switch_x + 1.0], [switch_y, switch_y], 'k-', lw=2)
        if switch_closed:
            ax.plot([switch_x + 0.5, switch_x + 0.5], [switch_y, switch_y + 0.7], 'k-', lw=2)
        else:
            ax.plot([switch_x + 0.5, switch_x + 0.3], [switch_y, switch_y + 0.5], 'k-', lw=2)
        ax.text(switch_x + 0.5, switch_y + 0.9, '开关', fontsize=12, ha='center', va='center', color='darkgreen')
        
        # 滑动变阻器
        resistor_x, resistor_y = 4.5, 2.5
        for i in range(10):
            x = resistor_x + i * 0.3
            ax.plot([x, x], [resistor_y - 0.6, resistor_y + 0.6], 'k-', lw=1)
        slider_pos = resistor_x + 0.3 + (slider_resistance / 20) * 2.4
        ax.plot([slider_pos - 0.4, slider_pos + 0.4], [resistor_y + 0.9, resistor_y + 0.9], 'k-', lw=2)
        ax.plot([slider_pos, slider_pos], [resistor_y + 0.9, resistor_y + 0.6], 'k-', lw=2)
        ax.text(resistor_x + 1.35, resistor_y + 1.2, '滑动变阻器', fontsize=12, ha='center', va='center', color='purple')
        ax.text(resistor_x + 1.35, resistor_y - 0.9, f'阻值: {slider_resistance:.1f}Ω', fontsize=10, ha='center', va='center', color='darkblue')
        
        # 定值电阻
        fixed_x, fixed_y = 8.0, 2.5
        ax.plot([fixed_x - 0.3, fixed_x - 0.15, fixed_x + 0.15, fixed_x + 0.3], 
                [fixed_y, fixed_y + 0.4, fixed_y - 0.4, fixed_y], 'k-', lw=2)
        ax.text(fixed_x, fixed_y - 0.57, '定值电阻', fontsize=12, ha='center', va='center', color='brown')
        ax.text(fixed_x, fixed_y - 0.9, f'{fixed_resistor}Ω', fontsize=10, ha='center', va='center', color='darkblue')
        
        # 电流表
        ammeter_x, ammeter_y = 10.0, 2.5
        ax.add_patch(plt.Circle((ammeter_x, ammeter_y), 0.5, fill=False, lw=2, edgecolor='blue'))
        ax.plot([ammeter_x - 0.5, ammeter_x + 0.5], [ammeter_y, ammeter_y], 'k-', lw=1)
        ax.text(ammeter_x, ammeter_y, 'A', fontsize=14, ha='center', va='center', fontweight='bold')
        ax.text(ammeter_x, ammeter_y + 0.9, '电流表', fontsize=12, ha='center', va='center', color='blue')
        
        # 电压表
        voltmeter_x, voltmeter_y = 8.0, 5.0
        ax.add_patch(plt.Circle((voltmeter_x, voltmeter_y), 0.5, fill=False, lw=2, edgecolor='red'))
        ax.plot([voltmeter_x - 0.5, voltmeter_x + 0.5], [voltmeter_y, voltmeter_y], 'k-', lw=1)
        ax.text(voltmeter_x, voltmeter_y, 'V', fontsize=14, ha='center', va='center', fontweight='bold')
        ax.text(voltmeter_x, voltmeter_y + 0.9, '电压表', fontsize=12, ha='center', va='center', color='red')
        
        # 导线（蓝色主线路）
        ax.plot([0.75, 0.75], [3.4, 4.5], 'b-', lw=2)
        ax.plot([0.75, 2.5], [4.5, 4.5], 'b-', lw=2)
        ax.plot([2.5, 2.5], [4.5, 2.5], 'b-', lw=2)
        ax.plot([3.5, 4.5], [2.5, 2.5], 'b-', lw=2)
        ax.plot([6.9, 7.7], [2.5, 2.5], 'b-', lw=2)
        ax.plot([8.3, 9.5], [2.5, 2.5], 'b-', lw=2)
        ax.plot([10.0, 10.0], [2.5, 0.5], 'b-', lw=2)
        ax.plot([10.0, 0.75], [0.5, 0.5], 'b-', lw=2)
        ax.plot([0.75, 0.75], [0.5, 1.1], 'b-', lw=2)

        # 电压表并联线路
        ax.plot([7.7, 7.7], [2.5, 4.5], 'r-', lw=2)
        ax.plot([7.7, 8.0], [4.5, 4.5], 'r-', lw=2)
        ax.plot([8.3, 8.3], [2.5, 4.5], 'r-', lw=2)
        ax.plot([8.0, 8.3], [4.5, 4.5], 'r-', lw=2)
        ax.plot([8.0, 8.0], [4.5, 4.7], 'r-', lw=2)
        ax.plot([8.3, 8.3], [4.5, 4.7], 'r-', lw=2)
        ax.plot([7.5, 8.5], [5.0, 5.0], 'r-', lw=1)
        
        # 数值显示
        ax.text(1.2, 1.2, f'电源电压: {power_voltage}V', fontsize=12,
                bbox=dict(facecolor='lightyellow', alpha=0.7, edgecolor='gold'))
        ax.text(11, 2.5, f'电流: {current*1000:.1f}mA', fontsize=12,
                bbox=dict(facecolor='lightblue', alpha=0.7, edgecolor='blue'))
        ax.text(9, 5, f'电压: {voltage:.2f}V', fontsize=12,
                bbox=dict(facecolor='lightgreen', alpha=0.7, edgecolor='green'))
        status = "闭合" if switch_closed else "断开"
        color = "green" if switch_closed else "red"
        ax.text(2, 2, f'开关状态: {status}', fontsize=12, color=color,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))
        ax.text(3, -1.5, f'欧姆定律: I = U / R = {power_voltage}V / {fixed_resistor+slider_resistance:.1f}Ω = {current*1000:.1f}mA',
                fontsize=11, bbox=dict(facecolor='lavender', alpha=0.7))

    # 初始绘制
    draw_components()

    # 滑动变阻器滑块
    ax_slider = plt.axes([0.2, 0.15, 0.6, 0.03])
    slider = Slider(ax=ax_slider, label='滑动变阻器阻值 (Ω)', valmin=0, valmax=20,
                    valinit=slider_resistance, valstep=0.1)

    # 开关按钮
    ax_button = plt.axes([0.45, 0.1, 0.1, 0.04])
    button = Button(ax_button, '开关', color='lightgoldenrodyellow', hovercolor='lightblue')

    # 输入框：电源电压 & 定值电阻
    ax_voltage_input = plt.axes([0.2, 0.26, 0.2, 0.04])  # 提高位置
    text_voltage = TextBox(ax_voltage_input, '电源电压(V)设置', initial=str(power_voltage))

    ax_resistor_input = plt.axes([0.6,0.26, 0.2, 0.04])  # 提高位置
    text_resistor = TextBox(ax_resistor_input, '定值电阻(Ω)设置', initial=str(fixed_resistor))

    # 更新事件
    def update(val):
        nonlocal slider_resistance, current, voltage
        slider_resistance = slider.val
        current, voltage = calculate_values()
        draw_components()
        fig.canvas.draw_idle()


    def toggle_switch(event):
        nonlocal switch_closed, current, voltage  # 改这里，声明非局部变量
        switch_closed = not switch_closed
        current, voltage = calculate_values()
        draw_components()
        fig.canvas.draw_idle()


    def update_voltage(text):
        nonlocal power_voltage, current, voltage
        try:
            power_voltage = float(text)
            current, voltage = calculate_values()
            draw_components()
            fig.canvas.draw_idle()
        except ValueError:
            pass


    def update_fixed_resistor(text):
        nonlocal fixed_resistor, current, voltage
        try:
            fixed_resistor = float(text)
            current, voltage = calculate_values()
            draw_components()
            fig.canvas.draw_idle()
        except ValueError:
            pass


    slider.on_changed(update)
    button.on_clicked(toggle_switch)
    text_voltage.on_submit(update_voltage)
    text_resistor.on_submit(update_fixed_resistor)

    # 展示窗口
    plt.show()


root = tk.Tk()
root.title("欧姆定律仿真教具")
root.geometry("1000x700")

show_main_page()

root.mainloop()

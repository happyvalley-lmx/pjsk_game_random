import flet as ft
import time
import random
from pjsk import math_game, random_songs, load_path
math_musics = math_game(37,1)
lucky_num = 0
selected_list = []
def main(page: ft.Page):
    global lucky_num
    global selected_list
    global songs, songs_data, math_musics
    global page_totalcol, help_text
    songs = []
    songs_data = []

    def select_song(e):
        # 随机抽歌亮起
        global lucky_num
        global selected_list
        # 模拟随机抽选效果
        for k in range(20):
            for i in range(7):
                if i not in selected_list:
                    # 若为Pick模式，则使用黄色，否则使用红色(Ban模式)
                    if switch1.value:
                        songs[i].controls[0].border = ft.border.all(5, ft.colors.GREEN_800)
                    else:
                        songs[i].controls[0].border = ft.border.all(5, ft.colors.RED_800)
                    page.update()
                    time.sleep(0.01)
                    songs[i].controls[0].border = ft.border.all(5, ft.colors.WHITE70)
                    page.update()

        # 抽选其中一个亮起
        lucky_num = random.randint(0, 6)
        while lucky_num in selected_list:
            lucky_num = random.randint(0, 6)
        # print(f"value:{switch1.value}, lucky_num:{lucky_num}")
        if switch1.value:
            songs[lucky_num].controls[0].border = ft.border.all(5, ft.colors.GREEN_800)
        else:
            songs[lucky_num].controls[0].border = ft.border.all(5, ft.colors.RED_800)
        button2.disabled = False
        page.update()
        # print(selected_list)

    def select_click_song(e):
        # 直接点击container选择
        global lucky_num,selected_list
        select_id = e.control.content.value
        if e.control.border == ft.border.all(5, ft.colors.WHITE70):
            if switch1.value:
                e.control.border = ft.border.all(5, ft.colors.GREEN_900)
            else:
                e.control.border = ft.border.all(5, ft.colors.RED_900)
            selected_list.append(int(select_id))
        else:
            e.control.border = ft.border.all(5, ft.colors.WHITE70)
            selected_list.remove(int(select_id))
        if len(selected_list) == 5:
            button1.disabled = True
            button3.disabled = False
        else:
            button1.disabled = False
        page.update()

    def select_pick_song(e):
        # 随机抽歌后按键选择
        global lucky_num,selected_list
        if switch1.value:
            songs[lucky_num].controls[0].border = ft.border.all(5, ft.colors.GREEN_900)
        else:
            songs[lucky_num].controls[0].border = ft.border.all(5, ft.colors.RED_900)
        select_id = songs[lucky_num].controls[0].content.value
        button2.disabled = True
        selected_list.append(int(select_id))
        if len(selected_list) == 5:
            button1.disabled = True
            button3.disabled = False
        else:
            button1.disabled = False
        page.update()

    title_row = ft.Row(controls=[ft.Text("广西 BEMALOW 世界计划 比赛抽歌器(Ban & Pick 规则)",size=28,weight=ft.FontWeight.BOLD)],alignment=ft.MainAxisAlignment.CENTER)

    # 首次抽歌
    for i in range(7): 
        musicinfo = random_songs(math_musics,1)
        music_id = musicinfo[0][0]
        music_name = musicinfo[0][1]
        music_difficulty = musicinfo[0][2]
        music_level = musicinfo[0][3]
        music_assetbundleName = musicinfo[0][4]
        # music_jacket = load_path + f"\\assets\\jackets\\{music_assetbundleName}.png"  # for windows
        music_jacket = f"/jackets/{music_assetbundleName}.png" # for web
        content_id = ft.Text(f"{i}",visible=False)
        globals()["song"+str(i)] = ft.Container(
            content=content_id,
            margin=15,
            width=160,
            height=160,
            border=ft.border.all(5, ft.colors.WHITE70),
            border_radius=20,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE_900,
            ink=True,
            ink_color=ft.colors.WHITE,
            on_click=select_click_song,
            image_src=music_jacket,
            image_fit=ft.ImageFit.FILL,
            image_opacity=1
            )
        music_text = ft.Text(f"[{music_difficulty} {music_level}]{music_name}",size=14)
        song_col = ft.Column(controls=[globals()["song"+str(i)],music_text],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=0)
        songs.append(song_col)
        songs_data.append(musicinfo)
        # print(f"[{i}]{music_id}.{music_name}")
    song_row1 = ft.Row(controls=songs[0:4],alignment=ft.MainAxisAlignment.CENTER)
    song_row2 = ft.Row(controls=songs[4:7],alignment=ft.MainAxisAlignment.CENTER)

    def re_select_song(e):
        # 刷新曲目
        global math_musics
        if switch_apd.value:
            math_musics = math_game(int(max_level.value),int(min_level.value),"apd")
        else:
            math_musics = math_game(int(max_level.value),int(min_level.value))
        global selected_list
        global songs_data
        selected_list=[]
        global songs,page_totalcol,help_text
        songs.clear()
        for i in range(7):
            musicinfo = random_songs(math_musics,1)
            music_id = musicinfo[0][0]
            music_name = musicinfo[0][1]
            music_difficulty = musicinfo[0][2]
            music_level = musicinfo[0][3]
            music_assetbundleName = musicinfo[0][4]
            # music_jacket = load_path + f"\\assets\\jackets\\{music_assetbundleName}.png"
            music_jacket = f"/jackets/{music_assetbundleName}.png" # for web
            content_id = ft.Text(f"{i}",visible=False)
            globals()["song"+str(i)] = ft.Container(
                content=content_id,
                margin=15,
                width=160,
                height=160,
                border=ft.border.all(5, ft.colors.WHITE70),
                border_radius=20,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLUE_900,
                ink=True,
                ink_color=ft.colors.WHITE,
                on_click=select_click_song,
                image_src=music_jacket,
                image_fit=ft.ImageFit.FILL,
                image_opacity=1
            )
            music_text = ft.Text(f"[{music_difficulty} {music_level}]{music_name}",size=14)
            song_col = ft.Column(controls=[globals()["song"+str(i)],music_text],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=0)
            songs.append(song_col)
            songs_data[i] = musicinfo
            # print(f"[{i}]{music_id}.{music_name}")
        song_row1 = ft.Row(controls=songs[0:4],alignment=ft.MainAxisAlignment.CENTER)
        song_row2 = ft.Row(controls=songs[4:7],alignment=ft.MainAxisAlignment.CENTER)
        page.remove(page_totalcol)
        txt_pause = ft.Text("这是一个断点")
        page.add(txt_pause)
        button1.disabled = False
        switch1.disabled = False
        help_text.controls[0].value = "使用方法：按钮切换ban/pick模式，点击乐曲封面可选择歌曲，选中框的颜色(红色/绿色)对应模式(ban/pick)，选够五首时可确认比赛曲目。"
        page_totalcol = ft.Column(controls=[title_row,song_row1,song_row2,button_row,difficulty_row,help_text],horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        page.add(page_totalcol)
        page.remove(txt_pause)
        # print(songs_data)

    def select_mode(e):
        # 开关切换ban/pick
        if switch1.value == False:
            button1.text = "随机选歌(Ban)"
            button2.text = "选择歌曲(Ban)"
        else:
            button1.text = "随机选歌(Pick)"
            button2.text = "选择歌曲(Pick)"
        page.update()

    def confirm_song(e):
        # 确认比赛曲目
        global songs_data, page_totalcol, help_text
        ban_songs = []
        ban_songs_container_list = []
        pick_songs = []
        pick_songs_container_list = []
        # 从全部选择id列表中获取单个id
        for selected_id in selected_list:
            song_container = globals()["song"+str(selected_id)]
            song_container.disabled = True
            musicinfo = songs_data[selected_id]
            music_name = musicinfo[0][1]
            music_difficulty = musicinfo[0][2]
            music_level = musicinfo[0][3]
            music_text = ft.Text(f"[{music_difficulty} {music_level}]{music_name}",size=14)
            song_col = ft.Column(controls=[song_container,music_text],horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=0)
            # 若果id为pick(识别边框绿色特征)，则添加到pick列表
            if songs[selected_id].controls[0].border == ft.border.all(5, ft.colors.GREEN_900):
                pick_songs.append(musicinfo)
                pick_songs_container_list.append(song_col)
            else:
                ban_songs.append(musicinfo)
                ban_songs_container_list.append(song_col)
        page.remove(page_totalcol)

        pick_songs_row = ft.Row(controls=pick_songs_container_list,alignment=ft.MainAxisAlignment.CENTER)
        ban_songs_row = ft.Row(controls=ban_songs_container_list,alignment=ft.MainAxisAlignment.CENTER)
        print(f"ban_songs:{ban_songs}\npick_songs:{pick_songs}")
        button3.disabled = True
        switch1.disabled = True
        help_text.controls[0].value = "比赛曲目已确认。"
        page_totalcol = ft.Column(controls=[title_row,pick_songs_row,ban_songs_row,button_row,difficulty_row,help_text],alignment=ft.CrossAxisAlignment.CENTER)
        page.add(page_totalcol)
    
    def only_append(e):
    # 开关切换仅append难度
        page.update()

    def check_level(e):
        # 检查难度值输入是否合理
        if min_level.value.isdigit() and min_level.value.isdigit():
            if min_level.value < max_level.value:
                if min_level.value != "" and max_level.value != "" :
                    button4.disabled = False
                    page.update()
                else:
                    button4.disabled = True
                    page.update()
            else:
                button4.disabled = True
                page.update()
        else:
            button4.disabled = True
            page.update()
    
    switch1 = ft.Switch(label="切换模式", value=False, on_change=select_mode)
    switch_apd = ft.Switch(label="仅append", value=False, on_change=only_append)

    button1 = ft.ElevatedButton(text="随机抽歌(Ban)",on_click=select_song)
    button2 = ft.ElevatedButton(text="选择歌曲(Ban)",on_click=select_pick_song,disabled=True)
    button3 = ft.ElevatedButton(text="确认",on_click=confirm_song,disabled=True)
    button4 = ft.ElevatedButton(text="刷新曲池",on_click=re_select_song,disabled=True)

    min_level = ft.TextField(label="最低难度",width=90,on_change=check_level)
    max_level = ft.TextField(label="最高难度",width=90,on_change=check_level)

    help_text = ft.Row([ft.Text("使用方法：按钮切换ban/pick模式，点击乐曲封面可选择歌曲，选够五首时可确认比赛曲目。",size=12)],alignment=ft.MainAxisAlignment.CENTER)

    button_row = ft.Row(controls=[switch1,button1,button2,button3],alignment=ft.MainAxisAlignment.CENTER)
    difficulty_row = ft.Row(controls=[switch_apd,min_level,max_level,button4],alignment=ft.MainAxisAlignment.CENTER)

    page_totalcol = ft.Column(controls=[title_row,song_row1,song_row2,button_row,difficulty_row,help_text],alignment=ft.CrossAxisAlignment.CENTER)

    page.window.max_height = 720
    page.window.max_width = 1280
    page.title = "广西 BEMALOW 世界计划 比赛抽歌器(Ban & Pick 规则)"
    page.add(page_totalcol)

ft.app(main, assets_dir="assets")

KV = '''


                       
<Demo>:
    manager: screen_manager
    Screen:
        BoxLayout:
            orientation:'vertical'
            MDTopAppBar:
                title: "Contacts Diary"
                elevation: 4
                pos_hint: {"top": 1}
                md_bg_color: "#e7e4c0"
                specific_text_color: "#4a4939"
                left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]  
               
            
            MDNavigationLayout:
                
                ScreenManager:
                    id: screen_manager
                    Screen:
                        name: "screen1"
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "15dp"
                            MDLabel:
                                text:'Security Guard'
                                size_hint: 1, 0.1
                                halign: 'center'
                
                            ScrollView:    
                                MDList:
                                    id: container  
                        MDFloatingActionButton:
                            icon : "plus"
                            pos_hint : {'center_x': 0.89,'center_y': 0.1}
                            on_release:
                                root.manager.current = 'add'                  
                    Screen:
                        name: "screen2"
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "15dp"
                            MDLabel:
                                text:'Gunner'
                                size_hint: 1, 0.1
                                halign: 'center'
                            
                            ScrollView:    
                                MDList:
                                    id: container1 
                                    
                        MDFloatingActionButton:
                            icon : "plus"
                            pos_hint : {'center_x': 0.89,'center_y': 0.1}
                            on_release:
                                root.manager.current = 'add'
                    Screen:
                        name: "add"
                        BoxLayout:
                            orientation: 'vertical'
                            padding: "15dp"
                            MDLabel:
                                text:'Add Contacts'
                                size_hint: 1, 0.5
                                halign: 'center'
                            MDTextField:
                                id:name
                                hint_text: "Enter Name"
                               
                                pos_hint:{'center_x': 0.5, 'center_y': 1}
                                size_hint_x:None
                                width:300

                            MDTextField:
                                id:number
                                hint_text: "Enter Phone Number"
                                max_text_length: 10
                                pos_hint:{'center_x': 0.5, 'center_y': 1}
                                size_hint_x:None
                                width:300
                                
                            
                            BoxLayout:
                                orientation: 'horizontal'
                                MDLabel:
                                    text: "Security Guard"
                                    halign: 'center'
                                MDCheckbox:
                                    id: checkbox_sg
                                    size_hint: None, None
                                    size: dp(48), dp(48)
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_active: app.update_securityguard(self.active)
                                MDLabel:
                                    text: "gunner"
                                    halign: 'center'
                                MDCheckbox:
                                    id: checkbox_gun
                                    size_hint: None, None
                                    size: dp(48), dp(48)
                                    pos_hint: {'center_x': .5, 'center_y': .5}
                                    on_active: app.update_gunner(self.active)
                                    
    
                                    
                            MDFlatButton:
                                text: 'Save' 
                                pos_hint:{'center_x': 0.5, 'center_y': 1}
                                on_press: 
                                    root.fun()   
                                    root.clear_text() 
                                    
                            MDLabel:
                                text:''               
                                
                                                  
        MDNavigationDrawer:
            id: nav_drawer 
            orientation: "vertical"
            padding: "50dp"
            spacing: "8dp"

            
            Content:
                manager: screen_manager
                nav_drawer: nav_drawer  
                
                
<Content>:
    
    ScrollView:
    
        MDList:
            id: box
            OneLineListItem:
                text:"Security Guard"
                on_release:
                    root.nav_drawer.set_state("close")
                    root.manager.current = 'screen1'
            OneLineListItem:
                text:"Gunner"  
                on_release:
                    root.nav_drawer.set_state("close")
                    root.manager.current = 'screen2'         
                            
                         
'''

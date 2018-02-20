from Screens.Screen import Screen
from Components.About import about
from Components.ActionMap import ActionMap
from Components.Button import Button
from Components.Label import Label
from enigma import getDesktop
from os import popen
import os
from enigma import eConsoleAppContainer, getDesktop
desktopSize = getDesktop(0).size()

class TSGeneralInfo(Screen):
    skin_1280 = '\n                <screen name="TSGeneralInfo" position="center,77" size="920,600"  title="General Info" >\n                    <widget name="DreamboxModel" position="85,35" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="FPVersion" position="85,65" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="EnigmaVersion" position="85,95" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="TSPanel" position="85,125" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="ImageVersion" position="85,155" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="Secondstage" position="85,185" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="DVBModules" position="85,215" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="Kernel" position="85,245" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="NetworkAdapter" position="85,275" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="IPAddress" position="85,305" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="MACAddress" position="85,335" size="800,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                    <widget name="Uptime" position="85,365" size="770,30" valign="top" halign="left" zPosition="-2" font="Regular;23" transparent="1"/>\n                  </screen>'
    skin_1920 = '    <screen name="TSGeneralInfo" position="center,200" size="1300,720" title="">\n        <widget name="DreamboxModel" position="20,20" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="FPVersion" position="20,60" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="EnigmaVersion" position="20,100" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="TSPanel" position="20,140" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="ImageVersion" position="20,180" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="Secondstage" position="20,220" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="DVBModules" position="20,260" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="Kernel" position="20,300" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="NetworkAdapter" position="20,340" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="IPAddress" position="20,380" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="MACAddress" position="20,420" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <widget name="Uptime" position="20,460" size="1260,40" foregroundColor="foreground" backgroundColor="background" font="Regular;28" valign="center" halign="left" transparent="1" zPosition="1" />\n        <ePixmap pixmap="/usr/lib/enigma2/python/Plugins/TSimage/TSimagePanel/images/tsimagelogo2.png" position="945,160" size="250,243" zPosition="-1" alphatest="blend" />\n        <widget source="global.CurrentTime" render="Label" position="840,50" size="460,70" font="Regular;65" halign="center" foregroundColor="foreground" backgroundColor="background" transparent="1">\n        <convert type="ClockToText">Default</convert>\n        </widget>\n        <widget source="session.CurrentService" render="Label" position="850,480" size="440,100" font="Regular;38" halign="center" foregroundColor="foreground" backgroundColor="background" transparent="1">\n        <convert type="ServiceName">Name</convert>\n        </widget>\n        </screen>'
    if desktopSize.width() == 1920:
        skin = skin_1920
    else:
        skin = skin_1280

    def __init__(self, session):
        Screen.__init__(self, session)
        model = self.getCmdOutput('cat /proc/stb/info/vumodel')
        self['VuplusModel'] = Label('Vuplus:\t\t %s' % model)
        self.enigmaVersion_text = 'Enigma2 Version:\t\t ' + about.getEnigmaVersionString()
        self['EnigmaVersion'] = Label(self.enigmaVersion_text)
        self['ImageVersion'] = Label('Image:\t\t ' + about.getImageVersionString())
        fp_version = None
        if fp_version is None:
            fp_version = ''
        else:
            fp_version = _('FP version:\t\t %d') % fp_version
        self['FPVersion'] = Label(fp_version)
        self['TSPanel'] = Label('TSPanel Version:\t\t %s' % '--------')
        self['DVBModules'] = Label('DVB-Modules:\t\t %s' % '--------')
        kernel = self.getCmdOutput('uname -r')
        self['Kernel'] = Label('Kernel:\t\t %s' % kernel)
        mac = self.getCmdOutput("ifconfig | grep HWaddr | awk '{print$5}'")
        ip = self.getCmdOutput("ifconfig | grep addr: | awk 'NR==1 {print$2}'")
        if ip == 'addr:127.0.0.1':
            ip = self.getCmdOutput("ifconfig | grep addr: | awk 'NR==2 {print$2}'")
            if ip == '':
                self.NetAdapter_text = 'Network Adapter:\t\t Disabled'
                ip = '--------'
                mac = '--------'
            else:
                tmp = self.getCmdOutput('ifconfig | grep ppp')
                if tmp == '':
                    self.NetAdapter_text = 'Network Adapter:\t\t WLAN'
                else:
                    self.NetAdapter_text = 'Network Adapter:\t\t PPP'
        else:
            self.NetAdapter_text = 'Network Adapter:\t\t LAN'
        self['NetworkAdapter'] = Label(self.NetAdapter_text)
        ip = ip.replace('addr:', '')
        self['IPAddress'] = Label('IP-Address:\t\t %s' % ip)
        self['MACAddress'] = Label('MAC-Address:\t\t %s' % mac)
        uptime_sec = float(self.getCmdOutput("cat /proc/uptime | awk '{print$1}'"))
        uptime = self.parse_time(uptime_sec)
        self['Uptime'] = Label('Uptime:\t\t %s' % uptime)
        self['key_red'] = Button(_('Close'))
        self['setupActions'] = ActionMap(['SetupActions'], {'ok': self.cancel,'cancel': self.cancel,
           'red': self.cancel
           })
        self.onShown.append(self.setWindowTitle)
        self.onLayoutFinish.append(self.loadDriverVU)
        return

    def setWindowTitle(self):
        self.setTitle(_('General Info'))

    def getCmdOutput(self, cmd):
        pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
        text = pipe.read()
        pipe.close()
        if text[-1:] == '\n':
            text = text[:-1]
        return text

    def loadDriverVU(self):
        cmd = "opkg list_installed | grep vuplus-dvb-modules | awk '{print$3}' > /tmp/driversinfo; opkg list_installed | grep tspanel | awk 'NR==1 {print$3}' > /tmp/panelinfo"
        self.container = eConsoleAppContainer()
        self.container.appClosed.append(self.UpdateGUI)
        self.container.execute(cmd)

    def UpdateGUI(self, result):
        print result
        panel = self.getCmdOutput('cat /tmp/panelinfo')
        self['TSPanel'].setText('TSPanel Version:\t\t %s' % panel.strip())
        drivers = self.getCmdOutput('cat /tmp/driversinfo')
        self['DVBModules'].setText('DVB-Modules:\t\t %s' % drivers)
        os.remove('/tmp/driversinfo')
        os.remove('/tmp/panelinfo')

    def parse_time(self, secs):
        res = []
        days, secs = divmod(int(secs), 86400)
        hours, secs = divmod(int(secs), 3600)
        mins, secs = divmod(int(secs), 60)
        res = '%dd %02d:%02d' % (days, hours, mins)
        return res

    def cancel(self):
        self.close()

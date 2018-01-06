def setTextColor(style, color, background, msg):
    return "\033[" + str(style) + ";"+ str(color) +";"+ str(background) +"m "+ str(msg) +" \033[0m"
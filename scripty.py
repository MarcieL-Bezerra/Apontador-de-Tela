from unicodedata import name
import pyautogui
import keyboard
from PIL import ImageGrab
from datetime import date
from screeninfo import get_monitors


def conver_to_Hex(r, g, b):
    rr = ""
    gg = ""
    bb = ""
    if r <= 15:
        rr = 0
    if g <= 15:
        gg = 0
    if b <= 15:
        bb = 0
    return ('#{}{:X}{}{:X}{}{:X}'). format(rr, r, gg, g, bb, b)


def conver_to_name(hexadecimal):
    try:
        Nome_da_Cor = {'#000000': 'Black - Preto', '#1C1C1C': 'grey11 - cinza11', '#363636': 'grey21 - cinza21', '#4F4F4F': 'grey31 - cinza31',
                    '#696969': 'DimGray - DimGray', '#808080': 'Gray - Cinza', '#A9A9A9': 'DarkGray - Cinza escuro', '#C0C0C0': 'Silver - Prata',
                    '#D3D3D3': 'LightGrey - Cinza claro', '#DCDCDC': 'Gainsboro - Gainsboro', '#6A5ACD': 'SlateBlue - Azul ardósia',
                    '#836FFF': 'SlateBlue1 - Ardósia Azul1', '#6959CD': 'SlateBlue3 - Ardósia Azul3', '#483D8B': 'DarkSlateBlue - DarkSlateBlue',
                    '#191970': 'MidnightBlue - Azul da meia noite', '#000080': 'Navy - Marinha', '#00008B': 'DarkBlue - Azul escuro',
                    '#0000CD': 'MediumBlue - MediumBlue', '#0000FF': 'Blue - Azul', '#6495ED': 'CornflowerBlue - Centáurea Azul',
                    '#4169E1': 'RoyalBlue - RoyalBlue', '#1E90FF': 'DodgerBlue - Trapaceiro azul', '#00BFFF': 'DeepSkyBlue - DeepSkyBlue',
                    '#87CEFA': 'LightSkyBlue - LightSkyBlue', '#87CEEB': 'SkyBlue - Céu azul', '#ADD8E6': 'LightBlue - Azul claro',
                    '#4682B4': 'SteelBlue - SteelBlue', '#B0C4DE': 'LightSteelBlue - LightSteelBlue', '#708090': 'SlateGray - Ardósia cinza',
                    '#778899': 'LightSlateGray - LightSlateGray', '#00FFFF': 'Aqua / Cyan - Aqua / Ciano', '#00CED1': 'DarkTurquoise - Turquesa Escuro',
                    '#40E0D0': 'Turquoise - Turquesa', '#48D1CC': 'MediumTurquoise - MédioTurquesa', '#20B2AA': 'LightSeaGreen - LightSeaGreen',
                    '#008B8B': 'DarkCyan - DarkCyan', '#008080': 'Teal - Cerceta', '#7FFFD4': 'Aquamarine - água-marinha',
                    '#66CDAA': 'MediumAquamarine - MédioAquamarine', '#5F9EA0': 'CadetBlue - CadetBlue', '#2F4F4F': 'DarkSlateGray - DarkSlateGray',
                    '#00FA9A': 'MediumSpringGreen - MédioPrimaveraVerde', '#00FF7F': 'SpringGreen - Primavera verde', '#98FB98': 'PaleGreen - Verde pálido',
                    '#90EE90': 'LightGreen - Luz verde', '#8FBC8F': 'DarkSeaGreen - DarkSeaGreen', '#3CB371': 'MediumSeaGreen - MédioMarVerde',
                    '#2E8B57': 'SeaGreen - Verde Mar', '#006400': 'DarkGreen - Verde escuro', '#008000': 'Green - Verde', '#228B22': 'ForestGreen - Verde floresta',
                    '#32CD32': 'LimeGreen - Verde limão', '#00FF00': 'Lime - Lima', '#7CFC00': 'LawnGreen - GramadoVerde', '#7FFF00': 'Chartreuse - Chartreuse',
                    '#ADFF2F': 'GreenYellow - Verde amarelo', '#9ACD32': 'YellowGreen - Amarelo verde', '6B8E23': 'OliveDrab - OliveDrab', '#556B2F': 'DarkOliveGreen - EscuroAzeitonaVerde',
                    '#808000': 'Olive - Oliva', '#BDB76B': 'DarkKhaki - DarkKhaki', '#DAA520': 'Goldenrod - Goldenrod', '#B8860B': 'DarkGoldenrod - DarkGoldenrod',
                    '#8B4513': 'SaddleBrown - Marrom Saddle', '#A0522D': 'Sienna - Siena', '#BC8F8F': 'RosyBrown - Marrom Rosado', '#CD853F': 'Peru - Peru',
                    '#D2691E': 'Chocolate - Chocolate', '#F4A460': 'SandyBrown - SandyBrown', '#FFDEAD': 'NavajoWhite - NavajoWhite', '#F5DEB3': 'Wheat - Trigo',
                                                                '#DEB887': 'BurlyWood - Madeira robusta', '#D2B48C': 'Tan - bronzeado', '#7B68EE': 'MediumSlateBlue - MediumSlateBlue', '#9370DB': 'MediumPurple - MédioRoxo',
                    '#8A2BE2': 'BlueViolet - AzulVioleta', '#4B0082': 'Indigo - Índigo', '#9400D3': 'DarkViolet - DarkViolet', '#9932CC': 'DarkOrchid - Orquídea Negra',
                    '#BA55D3': 'MediumOrchid - MédioOrquídea', '#A020F0': 'Purple - Roxo', '#8B008B': 'DarkMagenta - Dark Magenta', '#FF00FF': 'Fuchsia / Magenta - Fúcsia / Magenta',
                    '#EE82EE': 'Violet - Tolet', '#DA70D6': 'Orchid - Orquídea', '#DDA0DD': 'Plum - Ameixa', '#C71585': 'MediumVioletRed - MédioVioletaVermelho',
                    '#FF1493': 'DeepPink - Rosa escuro', '#FF69B4': 'HotPink - Rosa quente', '#DB7093': 'PaleVioletRed - PálidoVioletaVermelho',
                    '#FFB6C1': 'LightPink - Luz rosa', '#FFC0CB': 'Pink - Rosa', '#F08080': 'LightCoral - LightCoral', '#CD5C5C': 'IndianRed - Indian Red',
                    '#DC143C': 'Crimson - Carmesim', '#800000': 'Maroon - marrom', '#8B0000': 'DarkRed - Vermelho escuro', '#B22222': 'FireBrick - FireBrick',
                    '#A52A2A': 'Brown - Marrom', '#FA8072': 'Salmon - Salmão', '#E9967A': 'DarkSalmon - DarkSalmon', '#FFA07A': 'LightSalmon - LightSalmon',
                    '#FF7F50': 'Coral - Coral', '#FF6347': 'Tomato - Tomate', '#FF0000': 'Red - Vermelho', '#FF4500': 'OrangeRed - LaranjaVermelho', '#FF8C00': 'DarkOrange - Laranja escuro', '#FFA500': 'Orange - Laranja', '#FFD700': 'Gold - Ouro', '#FFFF00': 'Yellow - Amarelo', '#F0E68C': 'Khaki - cáqui', '#F0F8FF': 'AliceBlue - AliceBlue', '#F8F8FF': 'GhostWhite - Fantasma Branco', '#FFFAFA': 'Snow - Neve', '#FFF5EE': 'Seashell - Concha do mar', '#FFFAF0': 'FloralWhite - FloralBranco', '#F5F5F5': 'WhiteSmoke - Fumaça branca', '#F5F5DC': 'Beige - Bege', '#FDF5E6': 'OldLace - OldLace', '#FFFFF0': 'Ivory - Marfim', '#FAF0E6': 'Linen - Linho', '#FFF8DC': 'Cornsilk - Cornsilk', '#FAEBD7': 'AntiqueWhite - AntiqueWhite', '#FFEBCD': 'BlanchedAlmond - Amêndoa Branqueada', '#FFE4C4': 'Bisque - Bisque', '#FFFFE0': 'LightYellow - Luz amarela', '#FFFACD': 'LemonChiffon - Limão Chiffon', '#FAFAD2': 'LightGoldenrodYellow - LightGoldenrodYellow', '#FFEFD5': 'PapayaWhip - PapayaWhip', '#FFDAB9': 'PeachPuff - PeachPuff', '#FFE4B5': 'Moccasin - Mocassim', '#EEE8AA': 'PaleGoldenrod - PaleGoldenrod', '#FFE4E1': 'MistyRose - MistyRose', '#FFF0F5': 'LavenderBlush - LavandaBlush', '#E6E6FA': 'Lavender - Lavanda', '#D8BFD8': 'Thistle - Cardo', '#F0FFFF': 'Azure - Azure', '#E0FFFF': 'LightCyan - Ciano claro', '#B0E0E6': 'PowderBlue - Pó azul', '#E0FFFF': 'PaleTurquoise - ClaroTurquesa', '#F0FFF0': 'Honeydew - Melada', '#F5FFFA': 'MintCream - Creme de Menta'}
        nomeDaCor = Nome_da_Cor[hexadecimal]
        return nomeDaCor
    except:
        nomeDaCor = 'Nome não localizado'
        return nomeDaCor
    finally:
        return nomeDaCor


class funcoes:
    def __init__(self, x=1, y=""):
        self.x = x
        self.y = y

    def criarDados(self, pagina, TxPosX, TxPosY, TxRGB, TxHex, TxQtdTelas, TxData, TxColor, Txtnome):
        self.x, self.y = pyautogui.position()
        xt, yt = pyautogui.position()
        qtdTelas = 0
        for m in get_monitors():
            qtdTelas += 1
        while keyboard.is_pressed('q') == False:
            self.x, self.y = pyautogui.position()
            if (xt != self.x or yt != self.y):
                tela = ImageGrab.grab()  # Pega um print da tela
                # Pega a cor do pixel (x,y)
                area = tela.getpixel((self.x, self.y))
                hexagerado = conver_to_Hex(area[0], area[1], area[2])
                nomeDaCor = conver_to_name(hexagerado)
                xt = self.x
                yt = self.y
                data_atual = date.today()
                data_atual = data_atual.strftime('%d/%m/%Y')

                # alimentando as caixas
                TxPosX.delete(0, 'end')
                TxPosX.insert(0, self.x)
                TxPosY.delete(0, 'end')
                TxPosY.insert(0, self.y)
                TxRGB.delete(0, 'end')
                TxRGB.insert(0, area)
                TxHex.delete(0, 'end')
                Txtnome.delete(0, 'end')
                TxHex.insert(0, hexagerado)
                TxColor.config(background=hexagerado)
                Txtnome.insert(0, nomeDaCor)
                TxQtdTelas.delete(0, 'end')
                TxQtdTelas.insert(0, qtdTelas)
                TxData.delete(0, 'end')
                TxData.insert(0, data_atual)
                pagina.update()

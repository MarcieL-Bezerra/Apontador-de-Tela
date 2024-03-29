import tkinter as tk
from scripty import funcoes


class TelaInicial:
    def __init__(self ):
        self.criarTela()
        
    def sair(self):
        self.root.destroy()

    def valoresTxt(self):
        self.botaoSair.config(state =tk.DISABLED)
        text = funcoes.criarDados(self,pagina=self.root,TxPosX=self.TxPosX,TxPosY=self.TxPosY,TxRGB=self.TxRGB,TxHex=self.TxHex,TxQtdTelas=self.TxQtdTelas,TxData=self.TxData,TxColor=self.TxColor,Txtnome=self.Txnome)
        self.botaoSair.config(state =tk.NORMAL)
       
       


    def criarTela(self):
        #criar tela
        self.root = tk.Tk()
        self.root.title('Aponte o Mouse')
        self.root.geometry('600x430+100+50')
        self.root['bg'] = '#494646'
        self.root.iconphoto(True, tk.PhotoImage(file=r'.\\arquivos\\MB.png'))

        #frame posição
        fPosicao = tk.LabelFrame(self.root,width=20 , text="Posição do Mouse", bg="#000000", fg="white")
        fPosicao.grid(column=0, row=0, padx=20, pady=20)
        LblX = tk.Label(fPosicao,text='Posição de X ', width=10,justify='left', bg="#000000", fg="white",font=('arial',14,'bold'))
        LblX.grid(column=0,row=0, padx=10, pady=10)
        self.TxPosX=tk.Entry(fPosicao,width=6,justify='center',font=('arial',14,'bold'))
        self.TxPosX.grid(column=1,row=0, padx=10, pady=10)
        LblY= tk.Label(fPosicao,text='Posição de Y ',justify='left', bg="#000000", fg="white",font=('arial',14,'bold'))
        LblY.grid(column=0,row=1, padx=10, pady=10)
        self.TxPosY=tk.Entry(fPosicao,width=6,justify='center',font=('arial',14,'bold'))
        self.TxPosY.grid(column=1,row=1, padx=10, pady=10)

        #frame telas
        fTelas = tk.LabelFrame(self.root,text="Informação de Telas", bg="#000000", fg="white")
        fTelas.grid(column=1, row=0)
        LblT = tk.Label(fTelas,text='Qtd Telas ',justify='left', width=10,bg="#000000", fg="white",font=('arial',14,'bold'))
        LblT.grid(column=0,row=0, padx=10, pady=10)
        self.TxQtdTelas=tk.Entry(fTelas,width=6,justify='center',font=('arial',14,'bold'))
        self.TxQtdTelas.grid(column=1,row=0, padx=10, pady=10)
        LblY= tk.Label(fTelas,text='Data ',justify='left', bg="#000000", fg="white",font=('arial',14,'bold'))
        LblY.grid(column=0,row=1, padx=10, pady=10)
        self.TxData=tk.Entry(fTelas,width=10,justify='center',font=('arial',10,'bold'))
        self.TxData.grid(column=1,row=1, padx=10, pady=10)

        #frame cores
        fCores = tk.LabelFrame(self.root, text="Cores", bg="#000000", fg="white")
        fCores.grid(column=0, row=1, padx=20, pady=20)
        Lblnome = tk.Label(fCores,text='Nome',justify='left', bg="#000000", fg="white",font=('arial',12,'bold'))
        Lblnome.grid(column=0,row=0, padx=10, pady=10)
        self.Txnome=tk.Entry(fCores,width=20,justify='center',font=('arial',8,'bold'))
        self.Txnome.grid(column=1,row=0, padx=10, pady=10)
        LblRGB = tk.Label(fCores,text='Cores RGB ',justify='left', bg="#000000", fg="white",font=('arial',12,'bold'))
        LblRGB.grid(column=0,row=1, padx=10, pady=10)
        self.TxRGB=tk.Entry(fCores,width=10,justify='center',font=('arial',8,'bold'))
        self.TxRGB.grid(column=1,row=1, padx=10, pady=10)
        LblHex= tk.Label(fCores,text='Hexadecimal ',justify='left', bg="#000000", fg="white",font=('arial',12,'bold'))
        LblHex.grid(column=0,row=2, padx=10, pady=10)
        self.TxHex=tk.Entry(fCores,width=10,justify='center',font=('arial',8,'bold'))
        self.TxHex.grid(column=1,row=2, padx=10, pady=10)
        self.TxColor=tk.Entry(fCores,width=20,justify='center',font=('arial',14,'bold'))
        self.TxColor.grid(columnspan=2,row=3, padx=10, pady=10)

        #frame ajuda
        fAjudas = tk.LabelFrame(self.root, text="Informação de Telas", bg="#000000", fg="white")
        fAjudas.grid(column=1, row=1, padx=20, pady=20)

        lAjudas = tk.Label(fAjudas, text='Para congelar \n pressione a teclas "Q" ', width=18,height=5,bg="#000000", fg="white",font=('arial',14,'bold'))
        lAjudas.grid(column=0,row=0, padx=10, pady=15)

        self.botaoAbre = tk.Button(self.root, text="Descongelar",fg='white', width=12,bg='green',command=self.valoresTxt,font=('arial',14,'bold'))
        self.botaoAbre.place(relx=0.04,rely=0.9)

        self.botaoSair = tk.Button(self.root, text="Sair",fg='white',bg='green', width=12,command=self.sair,font=('arial',14,'bold'))
        self.botaoSair.place(relx=0.5,rely=0.9)
        
        self.valoresTxt()

        
        self.root.mainloop()
        









TelaInicial()
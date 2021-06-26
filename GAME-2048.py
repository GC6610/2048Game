from tkinter import Frame,Label,CENTER
import logic2048
import constants as c
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048 GAME')
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP:logic2048.move_up,
                       c.KEY_DOWN:logic2048.move_down,
                       c.KEY_LEFT:logic2048.move_left,
                       c.KEY_RIGHT:logic2048.move_right}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()
    def init_grid(self):
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOR_EMPTY_CELL,
                           width=c.SIZE/c.GRID_LEN,
                           height=c.SIZE/c.GRID_LEN)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_EMPTY_CELL,
                        justify=CENTER,font=c.FONT,width=8,height=3)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix=logic2048.start_game()
        logic2048.add_new_2(self.matrix)
        logic2048.add_new_2(self.matrix)
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(
                        text='',bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number), bg=c.BACKGROUND_COLOR_CELLS[new_number],
                        fg=c.CELL_COLOR_TEXT
                    )
        self.update_idletasks()
    def key_down(self,event):
        key=repr(event.char)
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                logic2048.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if logic2048.currgame(self.matrix)=='You won':
                    self.grid_cells[1][1].configure(
                        text="YOU",bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )
                    self.grid_cells[1][2].configure(
                        text="WIN!", bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )
                if logic2048.currgame(self.matrix)=='lost':
                    s=0
                    for i in self.matrix:
                        s+=sum(i)
                    self.grid_cells[1][1].configure(
                        text="YOU",bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )
                    self.grid_cells[1][2].configure(
                        text="LOST!", bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )
                    self.grid_cells[2][1].configure(
                        text="SCORE", bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )
                    self.grid_cells[2][2].configure(
                        text=str(s), bg=c.BACKGROUND_COLOR_EMPTY_CELL
                    )

gamegrid=Game2048()







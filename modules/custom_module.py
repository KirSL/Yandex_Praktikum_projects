import matplotlib.pyplot as plt

class Image:

    def __init__(self, width = 13, height = 4, dpi = 90, rotation = None, title = None, xlabel = None, ylabel = None, legend = False, grid = False):
        """Класс запоминает все необходимые параметры рисунка."""
        self.width = width
        self.height = height
        self.dpi = dpi
        self.rotation = rotation

        self.legend = legend
        self.grid = grid
        
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel


    def __enter__(self):
        """Вызывается на входе в конструкцию with."""
        plt.figure(figsize = (self.width, self.height), dpi = self.dpi)
    
    
    def __exit__(self, *args):
        """Вызывается на выходе из конструкции with."""
        if self.legend:
            plt.legend()
            
        if self.grid:
            plt.grid()
        
        
        plt.suptitle(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xticks(rotation = self.rotation)
        
        plt.show()
        plt.close()


        
## Проверка файла данных
def read_data(data_file, graphs = None, is_numeric_data = None):
    print(data_file.info())
    print('---\n')
    
    display(data_file.sample(5, random_state = 42))
    print('---\n')
    
    if is_numeric_data:
        print(data_file.describe())
        print('---\n')        
    
    if graphs:
        columns_list = data_file.columns

        for item in columns_list:
            if (data_file[item].dtypes) in ['int64','float64']:
                print(item.upper())

                data_file[item].hist(bins = 50,figsize = (10, 5))
                plt.show()

                data_file.boxplot(column=item)
                plt.show()
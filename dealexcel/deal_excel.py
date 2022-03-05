import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    """读取excel"""

    # 打开文件
    workbook = xlrd.open_workbook(r"C:\Users\peng\Desktop\report\base.xls", formatting_info=False)
    # 获取所有的sheet
    print("所有的工作表：",workbook.sheet_names())
    sheet1 = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)
    sheet1 = workbook.sheet_by_name("Sheet1")

    # 打印出所有合并的单元格
    print(sheet1.merged_cells)
    for (row,row_range,col,col_range) in sheet1.merged_cells:
        print(sheet1.cell_value(row,col))

    # sheet1的名称、行数、列数
    print("工作表名称：%s，行数：%d，列数：%d" % (sheet1.name, sheet1.nrows, sheet1.ncols))

    # 获取整行和整列的值
    row = sheet1.row_values(1)
    col = sheet1.col_values(4)
    print("第2行的值：%s" % row)
    print("第5列的值：%s" % col)

    # 获取单元格的内容
    print("第一行第一列：%s" % sheet1.cell(0,0).value)
    print("第一行第二列：%s" % sheet1.cell_value(0,1))
    print("第一行第三列：%s" % sheet1.row(0)[2])

    # 获取单元格内容的数据类型
    # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    print("第二行第三列的数据类型：%s" % sheet1.cell(3,2).ctype)

    # 判断ctype类型是否等于data，如果等于，则用时间格式处理
    if sheet1.cell(3,2).ctype == 3:
        data_value = xlrd.xldate_as_tuple(sheet1.cell_value(3, 2),workbook.datemode)
        print(data_value)
        print(date(*data_value[:3]))
        print(date(*data_value[:3]).strftime("%Y\%m\%d"))


def set_style(name,height,bold=False):
    """设置单元格样式"""
    style = xlwt.XFStyle()    # 初始化样式

    font = xlwt.Font()    # 为样式创建字体
    font.name = name    # 设置字体名字对应系统内字体
    font.bold = bold    # 是否加粗
    font.color_index = 5    # 设置字体颜色
    font.height = height    # 设置字体大小

    # 设置边框的大小
    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font    # 为样式设置字体
    style.borders = borders

    return style


def write_excel():
    """写入excel"""

    writeexcel = xlwt.Workbook()    # 创建工作表
    sheet1 = writeexcel.add_sheet(u"Sheet1", cell_overwrite_ok = True)    # 创建sheet

    row0 = ["编号", "姓名", "性别", "年龄", "生日", "学历"]
    num = [1, 2, 3, 4, 5, 6, 7, 8]
    column0 = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]
    education = ["小学", "初中", "高中", "大学"]

    # 生成合并单元格
    i,j = 1,0
    while i < 2*len(education) and j < len(education):
        sheet1.write_merge(i, i+1, 5, 5, education[j], set_style("Arial", 200, True))
        i += 2
        j += 1

    # 生成第一行
    for i in range(0, 6):
        sheet1.write(0, i, row0[i])

    # 生成前两列
    for i in range(1, 9):
        sheet1.write(i, 0, i)
        sheet1.write(i, 1, "a1")

    # 添加超链接
    n = "HYPERLINK"
    sheet1.write_merge(9,9,0,5,xlwt.Formula(n + '("https://www.baidu.com")'))

    # 保存文件
    writeexcel.save("demo.xls")


if __name__ == "__main__":
    read_excel()
    # write_excel()
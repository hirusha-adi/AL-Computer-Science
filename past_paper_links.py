codes = ['11', '12', '13']
seriess = ['s', 'w']
ptypes = ['qp', 'ms']

link = input("Enter a link: ")

full_part = link.split(".pdf")[0]
filename_no_ext = full_part.split("/")[-1]
filename_part = filename_no_ext.split("_")
link_no_filename = link.replace(link.split('/')[-1], '')



for series in seriess:
    for code in codes:
        for ptype in ptypes:
            new_filename = f"{filename_part[0]}_{series}{''.join(x for x in filename_part[1] if x.isdigit())}_{ptype}_{code}.pdf"
            print(link_no_filename + new_filename)

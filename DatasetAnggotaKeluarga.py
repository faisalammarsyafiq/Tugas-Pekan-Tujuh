import pandas as pd

pizza = {'Nama' : ['AGRI', 'ALDI NURUDIN', 'FATCHURROCHMAN', 'FITRIYANI SOLEHA', 'HELMI YAHYA SAPUTRA', 'WINA ROSALINA', 'YUGA WIRAPRATAMA', 'NONIK IKA NURFADILAH', 'YULIAH', 'ZAHRA SHIFA NURHALIZA', 'FAISAL AMMAR SYAFIQ', 'NOVAL AFIF SUJANA', 'MOCHAMAD YANUAR', 'SUGENG WIGUNA', 'WAHYU PURNOMO ADI', 'URIP', 'ILHAN IKSANI SYUKRI', 'AGUNG PRIYONO', 'RETNO WIDYA NUR AISYAH', 'AGUS JAKA SYAPUTRA MALAYA', 'FIFI YANTI', 'JOHAR', 'JUAN FAHRUL AMBIYAH', 'KARISMA BIMA SAKTI', 'MOHAMAD YEVAN ALFIANSYAH', 'NIAR RISMA AULIA', 'PUTU IBNU ARJANA', 'UCI TRI KHASANAH', 'LENDI PRASTYO'],
'Tinggi Badan' : [143, 155, 171, 147, 169, 142, 172, 158, 167, 159, 176, 178, 180, 171, 177, 165, 174, 160, 161, 170, 163, 174, 173, 170, 170, 159, 171, 166, 171],
'Berat Badan' : [51, 53, 67, 49, 58, 47, 66, 52, 57, 47, 78, 73, 82, 81, 68, 64, 93, 57, 57, 62, 68, 94, 68, 60, 63, 53, 72, 66, 68]
}

pizza_df = pd.DataFrame(pizza)
pizza_df
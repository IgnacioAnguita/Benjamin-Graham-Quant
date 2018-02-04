#Benjamin_Graham_Conservative_Investor
from io import open

class Business () : #creation of the class that will contain all the info about the business and calculate the tests and ratios
	def __init__(self, Name, MarketVal,Assets, Liabilities, Earnings10t, Dividends, Earnings, Earnings10, Price, BookVal):
		self.Name= Name #name of the business
		self.Market_Value=MarketVal #Market value
		self.Assets=Assets #total assets
		self.Liabilities=Liabilities #current liabilities
		self.Earnings_past_ten_years_test= Earnings10t #earnings through the last 10 years in a row
		self.Dividend_record_test= Dividends #Dividends paid through the last 20 years
		#all the earnings are referred to earnings per share
		self.Current_earnings=Earnings #current earnings
		self.Earnings_ten_years_ago =Earnings10 #earnings from ten years ago
		self.Price=Price #price of the business
		self.Book_value=BookVal #book value

	#calculation of ratios
		if self.Liabilities==0:
			self.Assets_liabilities_ratio=1 #to avoid having an error by dividing by 0
		else:
			self.Assets_liabilities_ratio = self.Assets/self.Liabilities #calculation of the Assets to liabilities ratio
	
		if self.Earnings_ten_years_ago==0:
			self.Earnings_growth_ratio = 1 #to avoid having an error by dividing by 0
		else:
			self.Earnings_growth_ratio = (self.Current_earnings-self.Earnings_ten_years_ago)/self.Earnings_ten_years_ago #calculation of the variation of growth
		if self.Current_earnings==0:
			self.P_E_ratio=1000 #to avoid having an error by dividing by 0 and also to avoid passing the P-E test
		else:
			self.P_E_ratio= self.Price/self.Current_earnings #calculation of the P/E ratio
		if self.Book_value==0:
			self.Price_to_Book_ratio=1000 #to avoid having an error by dividing by 0 and also to avoid passing the P-E test
			self.Error_Book_value=True #to print that we have an error in the book value
		else:
			self.Price_to_Book_ratio = self.Price/self.Book_value #calculation of the price-to-book ratio
		
	 	#calculation of the tests following Benjamin Graham advice for the defensive investor
		
		if self.Market_Value>2000000000: #Market capital bigger than 2e9
			self.Size_test=True
		else:
			self.Size_test=False
				
		if self.Assets_liabilities_ratio>2:
			self.Strong_financial_condition_test=True
		else:
			self.Strong_financial_condition_test=False
			
		if self.Earnings_growth_ratio>0.3:
			self.Earnings_growth_test= True
		else:
			self.Earnings_growth_test= False
	
		if self.P_E_ratio<=15:
			self.P_E_test=True
		else:
			self.P_E_test=False

		if self.Price_to_Book_ratio<=1.5:
			self.Price_to_Book_test =True
		else:
			self.Price_to_Book_test= False

		if self.Size_test==True and self.Strong_financial_condition_test==True and self.Earnings_past_ten_years_test==True and self.Dividend_record_test==True 	and self.Earnings_growth_test==True and self.P_E_test==True and self.Price_to_Book_test==True:
			self.Buy_test= True #if all the conditions are satisfied we can buy the stock
		else: 
			self.Buy_test=False
	def write_results(self): #here we write in the file the results of the tests
		Business_result_file=open("Business_result_file.txt","a")
		Business_result_file.write("\n" )
		Business_result_file.write(" \n")
		Business_result_file.write(self.Name)
		Business_result_file.write(" \n")
		Business_result_file.write(" Size test: ")
		Business_result_file.write(str(self.Size_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" Strong financial condition test:")
		Business_result_file.write(str(self.Strong_financial_condition_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" Earnings past ten years test: ")
		Business_result_file.write(str(self.Earnings_past_ten_years_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" Dividend record test: ")
		Business_result_file.write(str(self.Dividend_record_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" Earnings growth test: ")
		Business_result_file.write(str(self.Earnings_growth_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" P/E test: ")
		Business_result_file.write(str(self.P_E_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" Price to Book test: ")
		Business_result_file.write(str(self.Price_to_Book_test))
		Business_result_file.write(" \n")
		Business_result_file.write(" Buy test: ")
		Business_result_file.write(str(self.Buy_test))
		Business_result_file.write("\n" )
		Business_result_file.close()	

		

#extraction of the information about the companies
Business_info_file=open("Business_info_file_v0.txt","r")
text_lines=Business_info_file.readlines()

number_of_data=int(text_lines[0])*11
i=1;
while i<= number_of_data: # we pass the data of the txt file to the programm to calculate the ratios and do the tests
	Name=text_lines[i]
	i=i+1
	MarketVal=int(text_lines[i])
	i=i+1
	Assets=int(text_lines[i])
	i=i+1
	Liabilities=int(text_lines[i])
	i=i+1
	Earnings10t=int(text_lines[i])
	if Earnings10t== 1:
		Earnings10t=True
	else:
		Earnings10t=False
	i=i+1
	Dividends=int(text_lines[i])
	if Dividends== 1:
		Dividends=True
	else:
		Dividends=False
	i=i+1
	Earnings=float(text_lines[i])
	i=i+1
	Earnings10=float(text_lines[i])
	i=i+1
	Price=float(text_lines[i])
	i=i+1
	BookVal=float(text_lines[i])
	i=i+2
	B=Business(Name, MarketVal,Assets, Liabilities, Earnings10t, Dividends, Earnings, Earnings10, Price, BookVal) #we pass the info to the class
	B.write_results() #we write the results in the txt file

Business_info_file.close()


	

  
		
		



	
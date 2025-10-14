import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data dictionary for housing dataset
feature_dict = {
    "MSSubClass": "Identifies the type of dwelling involved in the sale",
    "MSZoning": "General zoning classification of the sale",
    "LotFrontage": "Linear feet of street connected to the property",
    "LotArea": "Lot size in square feet",
    "Street": "Type of road access to property",
    "Alley": "Type of alley access to property",
    "LotShape": "General shape of property",
    "LandContour": "Flatness of the property",
    "Utilities": "Type of utilities available",
    "LotConfig": "Lot configuration",
    "LandSlope": "Slope of property",
    "Neighborhood": "Physical locations within Ames city limits",
    "Condition1": "Proximity to various conditions",
    "Condition2": "Proximity to various conditions (if more than one is present)",
    "BldgType": "Type of dwelling",
    "HouseStyle": "Style of dwelling",
    "OverallQual": "Rates the overall material and finish of the house",
    "OverallCond": "Rates the overall condition of the house",
    "YearBuilt": "Original construction date",
    "YearRemodAdd": "Remodel date (same as construction date if no remodeling)",
    "RoofStyle": "Type of roof",
    "RoofMatl": "Roof material",
    "Exterior1st": "Exterior covering on the house",
    "Exterior2nd": "Exterior covering on house (if more than one material)",
    "MasVnrType": "Masonry veneer type",
    "MasVnrArea": "Masonry veneer area in square feet",
    "ExterQual": "Quality of exterior material",
    "ExterCond": "Condition of exterior material",
    "Foundation": "Type of foundation",
    "BsmtQual": "Height of the basement",
    "BsmtCond": "General condition of the basement",
    "BsmtExposure": "Walkout or garden-level wall exposure",
    "BsmtFinType1": "Rating of basement finished area",
    "BsmtFinSF1": "Type 1 finished square feet",
    "BsmtFinType2": "Rating of basement finished area (if multiple types)",
    "BsmtFinSF2": "Type 2 finished square feet",
    "BsmtUnfSF": "Unfinished square feet of basement area",
    "TotalBsmtSF": "Total square feet of basement area",
    "Heating": "Type of heating",
    "HeatingQC": "Heating quality and condition",
    "CentralAir": "Central air conditioning",
    "Electrical": "Electrical system",
    "1stFlrSF": "First floor square feet",
    "2ndFlrSF": "Second floor square feet",
    "LowQualFinSF": "Low-quality finished square feet (all floors)",
    "GrLivArea": "Above grade (ground) living area square feet",
    "BsmtFullBath": "Basement full bathrooms",
    "BsmtHalfBath": "Basement half bathrooms",
    "FullBath": "Full bathrooms above grade",
    "HalfBath": "Half bathrooms above grade",
    "Bedroom": "Bedrooms above grade (does NOT include basement bedrooms)",
    "Kitchen": "Kitchens above grade",
    "KitchenQual": "Kitchen quality",
    "TotRmsAbvGrd": "Total rooms above grade (does not include bathrooms)",
    "Functional": "Home functionality",
    "Fireplaces": "Number of fireplaces",
    "FireplaceQu": "Fireplace quality",
    "GarageType": "Garage location",
    "GarageYrBlt": "Year garage was built",
    "GarageFinish": "Interior finish of the garage",
    "GarageCars": "Size of garage in car capacity",
    "GarageArea": "Size of garage in square feet",
    "GarageQual": "Garage quality",
    "GarageCond": "Garage condition",
    "PavedDrive": "Paved driveway",
    "WoodDeckSF": "Wood deck area in square feet",
    "OpenPorchSF": "Open porch area in square feet",
    "EnclosedPorch": "Enclosed porch area in square feet",
    "3SsnPorch": "Three-season porch area in square feet",
    "ScreenPorch": "Screen porch area in square feet",
    "PoolArea": "Pool area in square feet",
    "PoolQC": "Pool quality",
    "Fence": "Fence quality",
    "MiscFeature": "Miscellaneous feature not covered in other categories",
    "MiscVal": "Value of miscellaneous feature",
    "MoSold": "Month sold",
    "YrSold": "Year sold",
    "SaleType": "Type of sale",
    "SaleCondition": "Condition of sale"
}

ms_subclass_details = [
    (20, "1-STORY 1946 & NEWER ALL STYLES"),
    (30, "1-STORY 1945 & OLDER"),
    (40, "1-STORY W/FINISHED ATTIC ALL AGES"),
    (45, "1-1/2 STORY - UNFINISHED ALL AGES"),
    (50, "1-1/2 STORY FINISHED ALL AGES"),
    (60, "2-STORY 1946 & NEWER"),
    (70, "2-STORY 1945 & OLDER"),
    (75, "2-1/2 STORY ALL AGES"),
    (80, "SPLIT OR MULTI-LEVEL"),
    (85, "SPLIT FOYER"),
    (90, "DUPLEX - ALL STYLES AND AGES"),
    (120, "1-STORY PUD (Planned Unit Development) - 1946 & NEWER"),
    (150, "1-1/2 STORY PUD - ALL AGES"),
    (160, "2-STORY PUD - 1946 & NEWER"),
    (180, "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER"),
    (190, "2 FAMILY CONVERSION - ALL STYLES AND AGES")
]

mszoning_details = [
    ("A", "Agriculture"),
    ("C", "Commercial"),
    ("FV", "Floating Village Residential"),
    ("I", "Industrial"),
    ("RH", "Residential High-Density"),
    ("RL", "Residential Low-Density"),
    ("RP", "Residential Low-Density Park"),
    ("RM", "Residential Medium Density"),
]

street_details = [
    ("Grvl", "Gravel"),
    ("Pave", "Paved"),
]

alley_details = [
    ("Grvl", "Gravel"),
    ("Pave", "Paved"),
    ("NA", "No alley access"),
]

lotshape_details = [
    ("Reg", "Regular"),
    ("IR1", "Slightly irregular"),
    ("IR2", "Moderately irregular"),
    ("IR3", "Irregular"),
]

landcontour_details = [
    ("Lvl", "Near Flat/Level"),
    ("Bnk", "Banked - rise from street grade"),
    ("HLS", "Hillside slope"),
    ("Low", "Depression"),
]

utilities_details = [
    ("AllPub", "All public Utilities (E,G,W,&S)"),
    ("NoSewr", "Electricity, Gas, Water (Septic Tank)"),
    ("NoSeWa", "Electricity and Gas Only"),
    ("ELO", "Electricity only"),
]

lotconfig_details = [
    ("Inside", "Inside lot"),
    ("Corner", "Corner lot"),
    ("CulDSac", "Cul-de-sac"),
    ("FR2", "Frontage on 2 sides"),
    ("FR3", "Frontage on 3 sides"),
]

landslope_details = [
    ("Gtl", "Gentle slope"),
    ("Mod", "Moderate slope"),
    ("Sev", "Severe slope"),
]

neighborhood_details = [
    ("Blmngtn", "Bloomington Heights"),
    ("Blueste", "Bluestem"),
    ("BrDale", "Briardale"),
    ("BrkSide", "Brookside"),
    ("ClearCr", "Clear Creek"),
    ("CollgCr", "College Creek"),
    ("Crawfor", "Crawford"),
    ("Edwards", "Edwards"),
    ("Gilbert", "Gilbert"),
    ("IDOTRR", "Iowa DOT and Rail Road"),
    ("MeadowV", "Meadow Village"),
    ("Mitchel", "Mitchell"),
    ("Names", "North Ames"),
    ("NoRidge", "Northridge"),
    ("NPkVill", "Northpark Villa"),
    ("NridgHt", "Northridge Heights"),
    ("NWAmes", "Northwest Ames"),
    ("OldTown", "Old Town"),
    ("SWISU", "South & West of ISU"),
    ("Sawyer", "Sawyer"),
    ("SawyerW", "Sawyer West"),
    ("Somerst", "Somerset"),
    ("StoneBr", "Stone Brook"),
    ("Timber", "Timberland"),
    ("Veenker", "Veenker"),
]

condition1_details = [
    ("Artery", "Adjacent to arterial street"),
    ("Feedr", "Adjacent to feeder street"),
    ("Norm", "Normal"),
    ("RRNn", "Within 200' of N-S Railroad"),
    ("RRAn", "Adjacent to N-S Railroad"),
    ("PosN", "Near positive off-site feature"),
    ("PosA", "Adjacent to positive off-site feature"),
    ("RRNe", "Within 200' of E-W Railroad"),
    ("RRAe", "Adjacent to E-W Railroad"),
]

bldgtype_details = [
    ("1Fam", "Single-family Detached"),
    ("2FmCon", "Two-family Conversion"),
    ("Duplx", "Duplex"),
    ("TwnhsE", "Townhouse End Unit"),
    ("TwnhsI", "Townhouse Inside Unit"),
]

housestyle_details = [
    ("1Story", "One story"),
    ("1.5Fin", "1.5 story: 2nd level finished"),
    ("1.5Unf", "1.5 story: 2nd level unfinished"),
    ("2Story", "Two-story"),
    ("2.5Fin", "2.5 story: 2nd level finished"),
    ("2.5Unf", "2.5 story: 2nd level unfinished"),
    ("SFoyer", "Split Foyer"),
    ("SLvl", "Split Level"),
]

overallqual_details = [(str(i), desc) for i, desc in [
    (10, "Very Excellent"), (9, "Excellent"), (8, "Very Good"), (7, "Good"),
    (6, "Above Average"), (5, "Average"), (4, "Below Average"),
    (3, "Fair"), (2, "Poor"), (1, "Very Poor")
]]

roofstyle_details = [
    ("Flat", "Flat"),
    ("Gable", "Gable"),
    ("Gambrel", "Gabrel (Barn)"),
    ("Hip", "Hip"),
    ("Mansard", "Mansard"),
    ("Shed", "Shed"),
]

roofmatl_details = [
    ("ClyTile", "Clay or Tile"),
    ("CompShg", "Standard (Composite) Shingle"),
    ("Membran", "Membrane"),
    ("Metal", "Metal"),
    ("Roll", "Roll"),
    ("Tar&Grv", "Gravel & Tar"),
    ("WdShake", "Wood Shakes"),
    ("WdShngl", "Wood Shingles"),
]

exterior1st_details = [
    ("AsbShng", "Asbestos Shingles"),
    ("AsphShn", "Asphalt Shingles"),
    ("BrkComm", "Brick Common"),
    ("BrkFace", "Brick Face"),
    ("CBlock", "Cinder Block"),
    ("CemntBd", "Cement Board"),
    ("HdBoard", "Hard Board"),
    ("ImStucc", "Imitation Stucco"),
    ("MetalSd", "Metal Siding"),
    ("Other", "Other"),
    ("Plywood", "Plywood"),
    ("PreCast", "PreCast"),
    ("Stone", "Stone"),
    ("Stucco", "Stucco"),
    ("VinylSd", "Vinyl Siding"),
    ("Wd Sdng", "Wood Siding"),
    ("WdShing", "Wood Shingles"),
]

masvnrtype_details = [
    ("BrkCmn", "Brick Common"),
    ("BrkFace", "Brick Face"),
    ("CBlock", "Cinder Block"),
    ("None", "None"),
    ("Stone", "Stone"),
]

exterqual_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Average/Typical"),
    ("Fa", "Fair"),
    ("Po", "Poor"),
]

foundation_details = [
    ("BrkTil", "Brick & Tile"),
    ("CBlock", "Cinder Block"),
    ("PConc", "Poured Concrete"),
    ("Slab", "Slab"),
    ("Stone", "Stone"),
    ("Wood", "Wood"),
]

bsmtqual_details = [
    ("Ex", "Excellent (100+ inches)"),
    ("Gd", "Good (90-99 inches)"),
    ("TA", "Typical (80-89 inches)"),
    ("Fa", "Fair (70-79 inches)"),
    ("Po", "Poor (<70 inches)"),
    ("NA", "No Basement"),
]

bsmtcond_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Typical - slight dampness allowed"),
    ("Fa", "Fair - dampness or some cracking"),
    ("Po", "Poor - severe cracking/settling"),
    ("NA", "No Basement"),
]

bsmtexposure_details = [
    ("Gd", "Good Exposure"),
    ("Av", "Average Exposure"),
    ("Mn", "Minimum Exposure"),
    ("No", "No Exposure"),
    ("NA", "No Basement"),
]

bsmtfintype1_details = [
    ("GLQ", "Good Living Quarters"),
    ("ALQ", "Average Living Quarters"),
    ("BLQ", "Below Average Living Quarters"),
    ("Rec", "Average Rec Room"),
    ("LwQ", "Low Quality"),
    ("Unf", "Unfinished"),
    ("NA", "No Basement"),
]

heating_details = [
    ("Floor", "Floor Furnace"),
    ("GasA", "Gas forced warm air furnace"),
    ("GasW", "Gas hot water or steam heat"),
    ("Grav", "Gravity furnace"),
    ("OthW", "Hot water/steam heat other than gas"),
    ("Wall", "Wall furnace"),
]

heatingqc_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Average/Typical"),
    ("Fa", "Fair"),
    ("Po", "Poor"),
]

centralair_details = [
    ("Y", "Yes"),
    ("N", "No"),
]

electrical_details = [
    ("SBrkr", "Standard Circuit Breakers & Romex"),
    ("FuseA", "Fuse Box >60 AMP, Romex wiring (Average)"),
    ("FuseF", "60 AMP Fuse Box, mostly Romex (Fair)"),
    ("FuseP", "60 AMP Fuse Box, knob & tube wiring (Poor)"),
    ("Mix", "Mixed"),
]

kitchenqual_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Typical/Average"),
    ("Fa", "Fair"),
    ("Po", "Poor"),
]

functional_details = [
    ("Typ", "Typical Functionality"),
    ("Min1", "Minor Deductions 1"),
    ("Min2", "Minor Deductions 2"),
    ("Mod", "Moderate Deductions"),
    ("Maj1", "Major Deductions 1"),
    ("Maj2", "Major Deductions 2"),
    ("Sev", "Severely Damaged"),
    ("Sal", "Salvage only"),
]

fireplacequ_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Average"),
    ("Fa", "Fair"),
    ("Po", "Poor"),
    ("NA", "No Fireplace"),
]

garagetype_details = [
    ("2Types", "More than one type of garage"),
    ("Attchd", "Attached to home"),
    ("Basment", "Basement Garage"),
    ("BuiltIn", "Built-In"),
    ("CarPort", "Car Port"),
    ("Detchd", "Detached"),
    ("NA", "No Garage"),
]

garagefinish_details = [
    ("Fin", "Finished"),
    ("RFn", "Rough Finished"),
    ("Unf", "Unfinished"),
    ("NA", "No Garage"),
]

garagequal_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Typical/Average"),
    ("Fa", "Fair"),
    ("Po", "Poor"),
    ("NA", "No Garage"),
]

paveddrive_details = [
    ("Y", "Paved"),
    ("P", "Partial Pavement"),
    ("N", "Dirt/Gravel"),
]

fence_details = [
    ("GdPrv", "Good Privacy"),
    ("MnPrv", "Minimum Privacy"),
    ("GdWo", "Good Wood"),
    ("MnWw", "Minimum Wood/Wire"),
    ("NA", "No Fence"),
]

poolqc_details = [
    ("Ex", "Excellent"),
    ("Gd", "Good"),
    ("TA", "Average/Typical"),
    ("Fa", "Fair"),
    ("NA", "No Pool"),
]

miscfeature_details = [
    ("Elev", "Elevator"),
    ("Gar2", "2nd Garage"),
    ("Othr", "Other"),
    ("Shed", "Shed (over 100 SF)"),
    ("TenC", "Tennis Court"),
    ("NA", "None"),
]

saletype_details = [
    ("WD", "Warranty Deed - Conventional"),
    ("CWD", "Warranty Deed - Cash"),
    ("VWD", "Warranty Deed - VA Loan"),
    ("New", "Home just constructed and sold"),
    ("COD", "Court Officer Deed/Estate"),
    ("Con", "Contract 15% Down payment regular terms"),
    ("ConLw", "Contract Low Down payment and low interest"),
    ("ConLI", "Contract Low Interest"),
    ("ConLD", "Contract Low Down"),
    ("Oth", "Other"),
]

salecondition_details = [
    ("Normal", "Normal Sale"),
    ("Abnorml", "Abnormal Sale - trade, foreclosure, short sale"),
    ("AdjLand", "Adjoining Land Purchase"),
    ("Alloca", "Allocation - linked properties"),
    ("Family", "Sale between family members"),
    ("Partial", "Home not completed when last assessed"),
]

# File paths+
CSV_PATH = os.path.join(BASE_DIR, 'data', 'housing_data.csv')
XLSX_PATH = os.path.join(BASE_DIR, 'data', 'housing_data.xlsx')
ASSETS_UNI_IMG_PATH = os.path.join(BASE_DIR, 'assets', 'images', 'univariate')
ASSETS_BI_IMG_PATH = os.path.join(BASE_DIR, 'assets', 'images', 'bivariate')
ASSETS_MUL_IMG_PATH = os.path.join(BASE_DIR, 'assets', 'images', 'multivariate')
ASSETS_FE_IMG_PATH = os.path.join(BASE_DIR, 'assets', 'images', 'feature_engineering')
MT_IMG_DIR = os.path.join(BASE_DIR, 'assets', 'images', 'market_trends')
CP_IMG_DIR = os.path.join(BASE_DIR, 'assets', 'images', 'customer_prefs')


# Sheet names
SHEET_HOUSING = 'Housing Data'
SHEET_MISSING = 'Missing Feature Analysis'
SHEET_FEATURE_ENGG = 'Feature Engineering'
SHEET_UNIVARIATE = 'Univariate Analysis'
SHEET_BIVARIATE = 'Bivariate Analysis'
SHEET_MULTIVARIATE = 'Multivariate Analysis'
SHEET_DICTIONARY = 'Data Dictionary'
SHEET_MSSUBCLASS = 'MSSubClass ChartData'
SHEET_MARKET_TRENDS = 'Market Trends'
SHEET_CUSTOMER_PREFSS ='Customer Preferences'
SHEET_OUTLIERS_REPORT = 'Outlier Report'
SHEET_DROPPED_FEATURES = 'Dropped Features'
SHEET_MISSING_DATA_VIZ = 'Missing Data Visualization'
SHEET_SUMMARY_STATS = 'Summary Statistics'
SHEET_CORRELATION = 'Correlation Matrix'
SHEET_PIVOT_TABLES = 'Pivot Tables'
SHEET_VISUALIZATIONS = 'Visualizations'
SHEET_FEATURE_IMPORTANCE = 'Feature Importance'
SHEET_MODEL_EVALUATION = 'Model Evaluation'
SHEET_NOTES = 'Notes'

# Header Names
MULTIVARIATE_ANALYSIS_HEADER = 'Multivariate Analysis Report'
FEATURE_ENGINEERING_HEADER = 'Feature Engineering Report'
MISSING_DATA_HEADER = 'Missing Data Analysis Report'
UNIVARIATE_ANALYSIS_HEADER = 'Univariate Analysis Report'
BIVARIATE_ANALYSIS_HEADER = 'Bivariate Analysis Report'
OUTLIER_ANALYSIS_HEADER = 'Outlier Analysis Report'
DROPPED_FEATURES_HEADER = 'Dropped Features Report'

UNIVARIATE_ANALYSIS = 'Univariate Analysis'
BIVARIATE_ANALYSIS = 'Bivariate Analysis'
MULTIVARIATE_ANALYSIS = 'Multivariate Analysis'
OUTLIER_ANALYSIS = 'Outlier Analysis'
DROPPED_FEATURES = 'Dropped Features'

# Header colors
COLOR_TEAL = '#00796B'
COLOR_NAVY = '#1F4E78'

# Chart settings
CHART_TITLE = 'Missing Data by Feature'
CHART_X_AXIS = 'Percentage (%)'
CHART_Y_AXIS = 'Feature'

# Chart Names
PAIR_PLOT_IMG = 'pairplot_matrix.png'
HEATMAP_IMG = 'correlation_heatmap.png'


# Threshold for missing data visualization
DROP_THRESHOLD = 0.50
MEAN_THRESHOLD = (0.05, 0.10)
MEDIAN_THRESHOLD = 0.30
import ROOT
import atlasplots as aplt
import numpy as np
import pandas as pd

aplt.set_atlas_style()

f = ROOT.TFile("QL2P11_3100V_2021-08-05_strip_position_analysis.root")
h = f.Get("xbin_width_100mm_ybin_width_100mm_means_layer2_fixedlayers13")

#  Canvas formatting
c = ROOT.TCanvas("c","c", 1000, 600)
c.cd()
c.SetRightMargin(0.15)

# Histogram axis
# h.GetYaxis().SetCanExtend(True)
# Histogram formatting
h.SetMaximum(0.5)
h.SetMinimum(-0.5)
h.GetZaxis().SetTitle("Mean residual from cosmics [mm]")
# h.GetZaxis().SetNdivisions(20)
h.Draw("colz")

palette = h.GetListOfFunctions().FindObject("palette")
palette.SetY2NDC(0.95)

# Confirmed these are right hist limits with QL2P08 formatted TH2F
# gLeft.GetXaxis().SetLimits(-1806/2.0, 1806/2.0)
# gLeft.GetHistogram().SetMaximum(1194.6)
# gLeft.GetHistogram().SetMinimum(0)

# Get the x-ray points
allData = pd.read_csv("QL2P11_xray_residuals.csv")
# Select only the layer 2, fixed layers 1 and 4 data
dataSubset = allData.loc[((allData['layer']==2) & (allData['fixed_layer_a']==1) & (allData['fixed_layer_b']==3)),['x', 'y', 'residual', 'residual error']]
print(dataSubset)
numPoints = len(dataSubset.index)

# testArrow proves that x1,y1,x2,y2 are in same coordinates as graph axes.
# testArrow = ROOT.TArrow(0,0,0,1194.6)
# testArrow.Draw()

arrows = []
annotations = []

for i in range(numPoints):
    # The x500 is a scale factor for drawing the arrow
    arrow = ROOT.TArrow(dataSubset['x'].iloc[i], dataSubset['y'].iloc[i], dataSubset['x'].iloc[i],
                        dataSubset['y'].iloc[i] + dataSubset['residual'].iloc[i]*500, 
                        0.01, ">")
    arrows.append(arrow)
    arrow.Draw()
    noteText = '  {:.2f}'.format(dataSubset['residual'].iloc[i])
    note = ROOT.TLatex(dataSubset['x'].iloc[i], dataSubset['y'].iloc[i], noteText)
    note.SetTextSize(20)
    annotations.append(note)
    note.Draw()



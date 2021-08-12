# Taking the cosmics mean residual TH2F from 2021-04-27 QL2C04 2900V, making it pretty,
# and printing the xray residuals on top of it.

import ROOT
import numpy as np
import pandas as pd
import atlasplots as aplt

aplt.set_atlas_style()
# c = ROOT.TCanvas("c", "c", 800, 600)
c = ROOT.TCanvas("c", "c")
c.cd()
c.SetRightMargin(0.15)

f = ROOT.TFile("QL2P11_3100V_2021-08-05_strip_position_analysis.root")
h = f.Get("xbin_width_100mm_ybin_width_100mm_means_layer2_fixedlayers13")
h.GetXaxis().SetLabelSize(55)
h.GetXaxis().SetTitleSize(55)
h.GetYaxis().SetLabelSize(55)
h.GetYaxis().SetTitleSize(55)
h.GetYaxis().SetTitleOffset(0.9)
h.GetZaxis().SetLabelSize(55)
h.GetZaxis().SetTitleSize(55)
h.GetZaxis().SetTitle("Mean cosmics residual [mm]")
h.Draw("colz")

# make palette same height as plot
palette = h.GetListOfFunctions().FindObject("palette")
palette.SetY2NDC(0.95)

# Add the xray points
allData = pd.read_csv("QL2P11_xray_residuals.csv")
# Select only the layer 2, fixed layers 1 and 4 data
dataSubset = allData.loc[((allData['layer']==2) & (allData['fixed_layer_a']==1) & (allData['fixed_layer_b']==3)),['x', 'y', 'residual', 'residual error']]
numPoints = len(dataSubset.index)
xGraph = ROOT.TGraph(numPoints, dataSubset['x'].to_numpy(), dataSubset['y'].to_numpy())
print(xGraph.GetMarkerSize())

# Make the xray labels
# annotations = [] # Note: not actually necessary
# for i in range(numPoints):
    # noteText =  {:1.2%}).format(dataSubset['residual'].iloc[i])) + "\pm" + str({:1.2%}).format(dataSubset['residual error'].iloc[i])
    # noteText = '{:.2f}\pm{:.2f}'.format(dataSubset['residual'].iloc[i], dataSubset['residual error'].iloc[i])
#    noteText = ' {:.2f}'.format(dataSubset['residual'].iloc[i])
#    print(noteText)
#    note = ROOT.TLatex(xGraph.GetX()[i], xGraph.GetY()[i], noteText)
#    note.SetTextSize(55)
#    xGraph.GetListOfFunctions().Add(note)
#    annotations.append(note)

h.Draw("colz")
xGraph.Draw("samep")

# c.SaveAs("figure_QL2P11_3100V_2021-08-05_fit_means_xray_overlay_layer2_fixedlayers13.pdf")
# c.SaveAs("figure_QL2P11_3100V_2021-08-05_fit_means_xray_overlay_layer2_fixedlayers13.root")

# aplt.atlas_label(text="Work in progress", loc="upper left", size=55)





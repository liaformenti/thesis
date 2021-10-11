import ROOT
import atlasplots as aplt

aplt.set_atlas_style()

# Get file
f = ROOT.TFile("QL2P08_3100V_2021-08-03_quick_sys_uncert_strip_position_analysis.root")

# Get desired plot
h = f.Get("xbin_width_100mm_ybin_width_100mm_means_layer4_fixedlayers13")

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

# aplt.atlas_label(text="Work in progress", loc="lower left")

# have to save canvas drawn with xming in full screen by hand to get proportions correct
c.Print("figure_QL2P08_3100V_2021-08-03_th2_means_layer4_fixedlayers13.pdf")
c.Print("figure_QL2P08_3100V_2021-08-03_th2_means_layer4_fixedlayers13.root")

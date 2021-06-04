import ROOT
import atlasplots as aplt

aplt.set_atlas_style()

inFile = ROOT.TFile("compare_residual_fits_QL2C04_2900V_2021-06-03_minus_quick_and_dirty_2900V_log_scale_layer1_fixedlayers34.root")
meanDiffs = inFile.Get("difference_in_residual_means")
sigmaDiffs = inFile.Get("difference_in_residual_sigmas")

c = ROOT.TCanvas("c","c")
c.Divide(2,1)
c.cd(1)
meanDiffs.Draw()
c.cd(2)
sigmaDiffs.Draw()




import ROOT
import atlasplots as aplt
import numpy as np

aplt.set_atlas_style()

# Get bin edges
xEdges = np.loadtxt("x_bin_edges.txt")
yEdges = np.loadtxt("y_bin_edges.txt")

# Prep histogram
xResTH2F = ROOT.TH2F("xResTH2F", "xResTH2F", len(xEdges)-1, xEdges, len(yEdges)-1, yEdges)

# Get xray residuals
# combinations holds layer,fixedlayerA,fixedlayerB
# positions holds x,y of residual (bin by this)
# residuals holds the residual, and the residual error
combinations = np.loadtxt("QL2P08_xray_residuals.txt",dtype='int',delimiter=',',skiprows=1,usecols=[0,1,2])
positions = np.loadtxt("QL2P08_xray_residuals.txt",dtype='float',delimiter=',',skiprows=1,usecols=[3,4])
residuals = np.loadtxt("QL2P08_xray_residuals.txt",dtype='float',delimiter=',',skiprows=1,usecols=[5,6])

# Fill with xray residuals
print("x,y,residual,residual error")
for i in range(len(residuals)):
    # For WNPPC, looking at layer 2, fixed layers 1, 4
    # Skip the residuals of other combinations
    if combinations[i,0] != 2: continue
    if combinations[i,1] != 1 or combinations[i,2] != 4: continue
    print(positions[i,0],positions[i,1],residuals[i,0],residuals[i,1])
    
    xResTH2F.Fill(positions[i,0],positions[i,1],residuals[i,0])

# Format canvas
c = ROOT.TCanvas("c","c")
c.cd()
c.SetRightMargin(0.15)

# Set all unfilled bins to an invalid number
# Based on unfilled bins being set to zero
# Also, label the xray residual value in bins with an xray residual
ts = []
for x in range(1, xResTH2F.GetNbinsX()+1):
    for y in range(1, xResTH2F.GetNbinsY()+1):
        if abs(xResTH2F.GetBinContent(x,y)) < 0.002: # this cutoff is spec to this data
                xResTH2F.SetBinContent(x,y,-100)
        else:
            t = ROOT.TText(xResTH2F.GetXaxis().GetBinCenter(x),
                           xResTH2F.GetYaxis().GetBinCenter(y),
                           "%4.3f" % xResTH2F.GetBinContent(x,y))
            ts.append(t)
            ts[-1].SetTextSize(29)
            ts[-1].SetTextAlign(22);


# Format histogram
xResTH2F.SetMaximum(0.2)
xResTH2F.SetMinimum(-0.2)
xResTH2F.GetXaxis().SetLabelSize(40)
xResTH2F.GetXaxis().SetTitleSize(40)
xResTH2F.GetYaxis().SetLabelSize(40)
xResTH2F.GetYaxis().SetTitleSize(40)
xResTH2F.GetZaxis().SetLabelSize(40)
xResTH2F.GetZaxis().SetTitleSize(40)
xResTH2F.GetXaxis().SetTitle("x [mm]")
xResTH2F.GetYaxis().SetTitle("y [mm]")
xResTH2F.GetZaxis().SetTitle("Residual from x-ray data [mm]")
xResTH2F.Draw("colz")

# Add labels to points
# ts = []
# for x in range(0, xResTH2F.GetNbinsX()+1):
#     for y in range(0, xResTH2F.GetNbinsY()+1):
#          
#         t = ROOT.TText(xResTH2F.GetXaxis().GetBinCenter(x),
#                       xResTH2F.GetYaxis().GetBinCenter(y),
#                       "%4.3f" % xResTH2F.GetBinContent(x,y))
#         ts.append(t)
#         ts[-1].SetTextSize(29)
#         ts[-1].SetTextAlign(22);

# Draw text
for t in ts:
    t.Draw()

#ROOT.gStyle.SetPaintTextFormat("4.3f")
# ROOT.gPad.Modified()
# ROOT.gPad.Update()
# palette = xResTH2F.GetListOfFunctions().FindObject("palette")
# print(palette.GetX1NDC(), palette.GetX2NDC(), palette.GetY1NDC(), palette.GetY2NDC())
# 
aplt.atlas_label(text="Work in progress", loc="upper left", size=40)

# Draw lines on histogram representing quad edges
# Hard coded
xTopLeft = -1806/2.0
yTopLeft = 1194.6
xTopRight = abs(xTopLeft)
yTopRight = yTopLeft
xBotLeft = xTopLeft + yTopLeft*np.tan(np.pi*(28/2)/180) 
yBotLeft = 0
xBotRight = xTopRight -yTopRight*np.tan(np.pi*(28/2)/180)
yBotRight = 0
# Left edge
xLeft = np.array([xTopLeft, xBotLeft])
yLeft = np.array([yTopLeft, yBotLeft])
gLeft = ROOT.TGraph(2, xLeft, yLeft)
gLeft.SetLineWidth(3)
gLeft.Draw("same")

xRight = np.array([xTopRight, xBotRight])
yRight = np.array([yTopRight, yBotRight])
gRight = ROOT.TGraph(2, xRight, yRight)
gRight.SetLineWidth(3)
gRight.Draw("same")

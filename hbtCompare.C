void hbt_compare(const char* fig_fname)
{
//=========Macro generated from canvas: t_canvas/v2
//=========  (Thu Sep 10 16:47:15 2009) by ROOT version5.22/00

 SetFlowStyle();

  TFile *f = TFile::Open(fig_fname);
  TGraphAsymmErrors *therm2 = (TGraphAsymmErrors*) f->Get("therm2");
  TGraphAsymmErrors *atlas = (TGraphAsymmErrors*) f->Get("atlas");


  
    //hist->Draw("glcol");


//BLUE
 therm2->SetMarkerStyle(22);
 therm2->SetMarkerSize(1.8);
 //therm2->SetMarkerColor(4);
 therm2->SetLineWidth(2);
 therm2->SetLineStyle(1);

 //therm2->SetFillColor(4);
 therm2->SetFillStyle(3001);
 therm2->SetLineColorAlpha(4,0.5);
 therm2->SetFillColorAlpha(4, 0.15);

//RED
 atlas->SetMarkerStyle(20);
 atlas->SetMarkerSize(1.3);

 atlas->SetLineWidth(1);
 atlas->SetLineStyle(1);
 atlas->SetLineColor(2);
 //atlas->SetFillColor(2);
 atlas->SetFillStyle(3001);
 atlas->SetMarkerColorAlpha(kRed+1, 0.8);
 atlas->SetFillColorAlpha(2, 0.5);

                        

 TCanvas *v2pt = new TCanvas("v2pt","",10,10,500,400);

 TPad *p1 = new TPad("p1","",.1,.1,.99,.95);
 p1->SetTopMargin(0.03);  
 p1->SetLeftMargin(0.2);  
 p1->SetBottomMargin(0.18);  
 p1->Draw();
 p1->cd();
 // p1->SetLogy();

 Double_t xmin = TMath::Min(therm2->GetXaxis()->GetXmin(), atlas->GetXaxis()->GetXmin());
 Double_t xmax = TMath::Max(therm2->GetXaxis()->GetXmax(), atlas->GetXaxis()->GetXmax());
 Double_t ymin = TMath::Min(therm2->GetYaxis()->GetXmin(), atlas->GetYaxis()->GetXmin());
 Double_t ymax = TMath::Max(therm2->GetYaxis()->GetXmax(), atlas->GetYaxis()->GetXmax());
 StyleHistogramVsPt(xmin, xmax, ymin, ymax)->Draw(); 


  //atlas->Draw("glcol");
  atlas->Draw("P5");
  //atlas->Draw("2");
  therm2->Draw("5");




  tex = new TLatex(320,-.17,"N_{part}");
   tex->SetTextSize(0.075);
   tex->SetLineWidth(2);
   tex->Draw();
   tex = new TLatex(-60,.12,"#rho(v_{2}^{2}, [p_{#perp}  ])");
   tex->SetTextSize(0.07);
   tex->SetTextAngle(90);
   tex->SetLineWidth(2);
   tex->Draw();
  

 TMarker* oo = new TMarker(30,.03,29);
oo->SetMarkerStyle(24);
 oo->SetMarkerColor(2);
 oo->SetMarkerSize(1.3);
 oo->Draw();
   tex = new TLatex(45,.02,"#Delta#eta_{p}=1 #Delta#eta_{v}=1.75");
   tex->SetTextSize(0.06);
   tex->SetLineWidth(2);
 tex->Draw();
 
 TMarker* oo = new TMarker(30,-.02,29);
oo->SetMarkerStyle(30);
 oo->SetMarkerColor(1);
 oo->SetMarkerSize(1.3);
 oo->Draw();
 tex = new TLatex(45,-.03,"#Delta#eta_{p}=0.4 #Delta#eta_{v}=0.75");
   tex->SetTextSize(0.06);
   tex->SetLineWidth(2);
 tex->Draw();


  TMarker* oo = new TMarker(30,-.065,22);
oo->SetMarkerStyle(22);
 oo->SetMarkerColor(4);
 oo->SetMarkerSize(1.8);
 oo->Draw(); 
 tex = new TLatex(45,-.075,"#Delta#eta_{p}=1 #Delta#eta_{v}=1.75 eff. 50%");
   tex->SetTextSize(0.06);
   tex->SetLineWidth(2);
   tex->Draw();
 
   tex = new TLatex(200,.25,"Pb-Pb   2.76 TeV");
   tex->SetTextSize(0.06);
   tex->SetLineWidth(2);
     tex->Draw();

   v2pt->Modified();
   v2pt->SaveAs("corrvptacc.png");
   v2pt->SaveAs("corrvptacc.eps");
   v2pt->SaveAs("corrvptacc.pdf");
}
   
// =====================================================================================

TH1D* StyleHistogramVsPt(Double_t xmin, Double_t xmax, Double_t ymin, Double_t ymax)
{
 // Style histogram:
 
 Int_t nBins = 100; // to be improved - hardwired 100
 Double_t ptMin = -3; // in [GeV/c] // to be improved - hardwired 0
 Double_t ptMax = 3; // in [GeV/c] // to be improved - hardwired 5.75
 TString xTitle  = "";
 //TString yTitle  = "v_{2}";
   
 TH1D* hist = new TH1D("","",nBins,xmin,xmax);
 // hist->SetXTitle(xTitle.Data());
 //hist->SetYTitle(yTitle.Data());
 hist->SetMinimum(ymin); // minimum y-value - to be improved
 hist->SetMaximum(ymax); // maximum y-value - to be improved
  hist->GetXaxis()->SetNdivisions(504);
  hist->GetYaxis()->SetNdivisions(506);
  hist->GetXaxis()->SetLabelSize(0.07);
  hist->GetYaxis()->SetLabelSize(0.07);

 // hist->GetXaxis()->SetTickLength(0.);
 hist->SetLineWidth(0);
 hist->SetLineColor(0);
 return hist;
 
} // end of TH1D* StyleHistogramVsPtDown()
  
// =====================================================================================



void SetFlowStyle()
{
 // Set style which will affect all plots.
 
 gStyle->Reset();

 gStyle->SetCanvasPreferGL(1);
 gStyle->SetPalette(1);

 // gStyle->SetOptitle(0);
 // gStyle->SetOptStat(0);
 //gStyle->SetOptDate(1);
 // gStyle->SetPalette(8,0);  // (1,0)
 gStyle->SetPalette(1);  // (1,0)
 gStyle->SetDrawBorder(0);
 // gStyle->SetFillColor(0);  // kills palete ???
 gStyle->SetCanvasColor(0);
 gStyle->SetPadColor(0);
 // gStyle->SetFillColor(0); // otherwize it affects Fill colors later
 gStyle->SetFrameFillColor(0);
 gStyle->SetCanvasBorderMode(0);
 gStyle->SetFrameLineWidth(2);
  gStyle->SetFrameFillStyle(4000);
 gStyle->SetPadBorderMode(0);
 gStyle->SetPadTickX(1);
 gStyle->SetPadTickY(1);
 gStyle->SetPadBottomMargin(0.15);
 gStyle->SetPadLeftMargin(0.19);
 gStyle->SetHistLineWidth(2);
 gStyle->SetFuncWidth(2);
 gStyle->SetLineWidth(2);
 gStyle->SetLabelSize(0.056,"xyz");
 gStyle->SetLabelOffset(0.01,"y");
 gStyle->SetLabelColor(kBlack,"xyz");
 gStyle->SetTitleSize(0.1,"xyz");
 gStyle->SetTitleOffset(1.3,"y");
 gStyle->SetTitleFillColor(0);
 gStyle->SetLineWidth(2);  
 gStyle->SetHistLineColor(1);
 gStyle->SetTextColor(1);
 gStyle->SetTitleTextColor(1);
 TGaxis::SetMaxDigits(4);
 gStyle->SetOptStat(0); // removes stat. box from all histos
 gROOT->ForceStyle();

} // end of void SetFlowStyle()



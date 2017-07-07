void hbtCompare(TString fig_fname, TString centrality)
{


TMap* yTitlesMap = new TMap(20,0);
yTitlesMap->Add(new TObjString("fig_23"), new TObjString("#it{R_{out}} [fm]"));
yTitlesMap->Add(new TObjString("fig_24"), new TObjString("#it{R_{side}} [fm]"));
yTitlesMap->Add(new TObjString("fig_25"), new TObjString("#it{R_{long}} [fm]"));
yTitlesMap->Add(new TObjString("fig_29"), new TObjString("#it{#lambda}"));
yTitlesMap->Add(new TObjString("fig_30"), new TObjString("#it{#frac{R_{out}}{R_{side}}}"));
yTitlesMap->Add(new TObjString("fig_34"), new TObjString("#it{R_{ol}} [fm]"));

TMap* labelsMap = new TMap(20,0);
labelsMap->Add(new TObjString("fig_23"), new TObjString("a)"));
labelsMap->Add(new TObjString("fig_24"), new TObjString("b)"));
labelsMap->Add(new TObjString("fig_25"), new TObjString("c)"));
labelsMap->Add(new TObjString("fig_34"), new TObjString("d)"));


TMap* centMap = new TMap(20,0);
centMap->Add(new TObjString("01"), new TObjString("0-1%"));
centMap->Add(new TObjString("1020"), new TObjString("10-20%"));
centMap->Add(new TObjString("4050"), new TObjString("40-50%"));

TString all_figs[] = {"fig_23a", "fig_23b", "fig_24a", "fig_24b", "fig_25a", "fig_25b", 
                      "fig_29a", "fig_29b", "fig_30a", "fig_30b", "fig_34a", "fig_34_kt"};

//for(int i=0; i<sizeof(all_figs)/sizeof(all_figs[0]); i++){
//    if fig_fname.Contains(all_figs[i]){
//        TString 
//    }
//}



TString yTitle("");
for(TIter it=TIter(yTitlesMap); next = it.Next(); ){ 
    TString nextkey( ((TObjString*)next)->String() );
    if ( fig_fname.Contains(nextkey.Data()) ){
        yTitle = ((TObjString*)yTitlesMap(nextkey))->String();
    }
}

TString labelText("");
for(TIter it=TIter(labelsMap); next = it.Next(); ){ 
    TString nextkey( ((TObjString*)next)->String() );
    if ( fig_fname.Contains(nextkey.Data()) ){
        labelText = ((TObjString*)labelsMap(nextkey))->String();
    }
}

if (fig_fname.Contains("34a.root")) const char* MODE = "VSy34";
else if (fig_fname.Contains("34_kt.root")) const char* MODE = "VSkt34";
else if (fig_fname.Contains("a.root")) const char* MODE = "VSkt"; 
else if (fig_fname.Contains("b.root")) const char* MODE = "VSy"; 
else{
    cout<<"ERROR: no '*a.root' or '*b.root' in 'fig_fname' (="<<fig_fname<<")\n";
	gApplication->Terminate();
}





 SetFlowStyle();


  TFile *f = TFile::Open(fig_fname);
  cout << "trying to open: "<< "therm"+centrality<<endl;
  TGraphAsymmErrors *therm = (TGraphAsymmErrors*) f->Get("therm"+centrality);
  TGraphAsymmErrors *atlas = (TGraphAsymmErrors*) f->Get("atlas"+centrality);


 therm->SetMarkerStyle(22);
 therm->SetMarkerSize(1.8);
 therm->SetLineWidth(2);
 therm->SetLineStyle(1);
 therm->SetFillStyle(1001);
 therm->SetLineColorAlpha(4,0.5);
 therm->SetFillColorAlpha(4, 0.15);


 atlas->SetMarkerStyle(20);
 atlas->SetMarkerSize(1.3);
 atlas->SetLineWidth(1);
 atlas->SetLineStyle(1);
 atlas->SetLineColor(2);
 atlas->SetFillStyle(1001);
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

// Double_t xmin = TMath::Min(therm->GetXaxis()->GetXmin(), atlas->GetXaxis()->GetXmin());
// Double_t xmax = TMath::Max(therm->GetXaxis()->GetXmax(), atlas->GetXaxis()->GetXmax());
 Double_t ymin = TMath::Floor(TMath::Min(therm->GetYaxis()->GetXmin(), atlas->GetYaxis()->GetXmin()));
 Double_t ymax = TMath::Ceil(TMath::Max(therm->GetYaxis()->GetXmax(), atlas->GetYaxis()->GetXmax()));



if (MODE == "VSkt"){
    StyleHistoVSkt(ymin, ymax, yTitle)->Draw(); 

    double legLeftPos = 0.25;
    double legBottomPos = 0.255;
    double sysLabelLeftPos = 0.24;
    double sysLabelBottomPos = 0.43;
    double rangeLabelLeftPos = 0.67;
    double rangeLabelBottomPos = 0.23;

	tex = new TLatex(rangeLabelLeftPos,rangeLabelBottomPos, "-1 < #it{y_{#pi#pi}} < 0");
	tex->SetNDC(kTRUE);
	tex->SetTextSize(0.055);
	tex->SetLineWidth(1);
	tex->Draw();
}
else if (MODE == "VSy"){
    StyleHistoVSy(ymin, ymax, yTitle)->Draw(); 

    double legLeftPos = 0.25;
    double legBottomPos = 0.255;
    double sysLabelLeftPos = 0.24;
    double sysLabelBottomPos = 0.43;
    double rangeLabelLeftPos = 0.565;
    double rangeLabelBottomPos = 0.23;

	tex = new TLatex(rangeLabelLeftPos,rangeLabelBottomPos, "0.2 < #it{k_{T}} < 0.3 GeV");
	tex->SetNDC(kTRUE);
	tex->SetTextSize(0.055);
	tex->SetLineWidth(1);
	tex->Draw();
}

else if (MODE == "VSy34"){
   TH1D* hist = StyleHistoVSy(ymin, ymax, yTitle);
   hist->SetMinimum(-0.25);
   hist->SetMaximum(0.3);
   hist->Draw(); 
  
    double legLeftPos = 0.58;
    double legBottomPos = 0.24;
    double sysLabelLeftPos = 0.24;
    double sysLabelBottomPos = 0.27;
    double rangeLabelLeftPos = 0.56;
    double rangeLabelBottomPos = 0.4;

	tex = new TLatex(rangeLabelLeftPos,rangeLabelBottomPos, "0.2 < #it{k_{T}} < 0.3 GeV");
	tex->SetNDC(kTRUE);
	tex->SetTextSize(0.055);
	tex->SetLineWidth(2);
	tex->Draw();
}

else if (MODE == "VSkt34"){
   TH1D* hist = StyleHistoVSkt(ymin, ymax, yTitle);
   hist->SetMinimum(0);
   hist->SetMaximum(0.15);
   hist->Draw(); 
  
    double legLeftPos = 0.25;
    double legBottomPos = 0.185;
    double sysLabelLeftPos = 0.24;
    double sysLabelBottomPos = 0.36;
    double rangeLabelLeftPos = 0.67;
    double rangeLabelBottomPos = 0.23;

	tex = new TLatex(rangeLabelLeftPos,rangeLabelBottomPos, "-1 < #it{y_{#pi#pi}} < 0");
	tex->SetNDC(kTRUE);
	tex->SetTextSize(0.055);
	tex->SetLineWidth(1);
	tex->Draw();
}



  atlas->Draw("P5");
  therm->Draw("5");


  tex = new TLatex(sysLabelLeftPos,sysLabelBottomPos, "#splitline{p+Pb "+((TObjString*)centMap(centrality))->String()+"}{#sqrt{s_{NN}} = 5.02 TeV}");
  tex->SetNDC(kTRUE);
  tex->SetTextSize(0.06);
  tex->SetLineWidth(2);
  tex->Draw();


 // LEGEND

 // hydro
 TMarker* oo = new TMarker(legLeftPos+0.01,legBottomPos+0.07,therm->GetMarkerStyle());
   oo->SetNDC(kTRUE);
   oo->SetMarkerStyle(21);
   oo->SetMarkerColorAlpha(4,0.15);
   oo->SetMarkerSize(2);
   oo->Draw();
 TMarker* oo = new TMarker(legLeftPos+0.01,legBottomPos+0.07,therm->GetMarkerStyle());
   oo->SetNDC(kTRUE);
   oo->SetMarkerStyle(25);
   oo->SetMarkerColorAlpha(4,0.5);
   oo->SetMarkerSize(2);
   oo->Draw();
 tex = new TLatex(legLeftPos+0.04,legBottomPos+0.05,"hydro model");
   tex->SetNDC(kTRUE);
   tex->SetTextSize(0.06);
   tex->SetLineWidth(1);
   tex->Draw();

 // atlas
 if (MODE != "VSkt34"){
	 TMarker* oo = new TMarker(legLeftPos+0.01,legBottomPos,atlas->GetMarkerStyle());
	   oo->SetNDC(kTRUE);
	   oo->SetMarkerStyle(21);
	   oo->SetMarkerColorAlpha(atlas->GetMarkerColor(),0.5);
	   oo->SetMarkerSize(2);
	   oo->Draw();
	 TMarker* oo = new TMarker(legLeftPos+0.01,legBottomPos,atlas->GetMarkerStyle());
	   oo->SetNDC(kTRUE);
	   oo->SetMarkerStyle(25);
	   oo->SetMarkerColorAlpha(atlas->GetMarkerColor(),0.8);
	   oo->SetMarkerSize(2);
	   oo->Draw();
	 TMarker* oo = new TMarker(legLeftPos+0.01,legBottomPos,atlas->GetMarkerStyle());
	   oo->SetNDC(kTRUE);
	   oo->SetMarkerStyle(atlas->GetMarkerStyle());
	   oo->SetMarkerColor(atlas->GetMarkerColor());
	   oo->SetMarkerSize(atlas->GetMarkerSize());
	   oo->Draw();
	 tex = new TLatex(legLeftPos+0.04,legBottomPos-0.025,"ATLAS data");
	   tex->SetNDC(kTRUE);
	   tex->SetTextSize(0.06);
	   tex->SetLineWidth(2);
	   tex->Draw();
 }




 tex = new TLatex(0.24,.87,labelText);
   tex->SetNDC(kTRUE);
   tex->SetTextSize(0.08);
   tex->SetLineWidth(2);
 tex->Draw();



   v2pt->Modified();
   TString outFigName(fig_fname);
   
   v2pt->SaveAs(outFigName.Replace(outFigName.Length()-5, 5, "_c"+centrality+".png"));
   v2pt->SaveAs(outFigName.Replace(outFigName.Length()-4, 4, ".pdf"));
   // v2pt->SaveAs(outFigName.Replace(outFigName.Length()-4, 4, ".eps"));

}
   

// =====================================================================================

TH1D* StyleHistoVSkt(Double_t ymin, Double_t ymax, TString yTitle)
{
 // Style histogram:
 
 TH1D* hist = new TH1D("","",10000,-2,2);

 hist->SetMinimum(0); // minimum y-value - to be improved
 hist->SetMaximum(ymax); // maximum y-value - to be improved

  hist->GetXaxis()->SetRangeUser(0,0.9);
  hist->GetXaxis()->SetNdivisions(505);
  if (TString(yTitle).Contains("#it{R_{o")) hist->GetYaxis()->SetNdivisions(505);
  else hist->GetYaxis()->SetNdivisions(510);
  hist->GetXaxis()->SetTitle("#it{k_{T}} [GeV]");
  hist->GetYaxis()->SetTitle(yTitle);
  hist->GetXaxis()->SetTitleOffset(1.1);
  hist->GetYaxis()->SetTitleOffset(1.1);
  hist->GetXaxis()->SetTitleSize(0.065);
  hist->GetYaxis()->SetTitleSize(0.065);
  hist->GetXaxis()->SetLabelSize(0.065);
  hist->GetYaxis()->SetLabelSize(0.065);


 hist->SetLineWidth(0);
 hist->SetLineColor(0);
 return hist;
 
} // end of TH1D* StyleHistoVSkt()
  
// =====================================================================================



TH1D* StyleHistoVSy(Double_t ymin, Double_t ymax, TString yTitle)
{
 // Style histogram:
 
 TH1D* hist = new TH1D("","",10000,-10,10);

 hist->SetMinimum(0); // minimum y-value - to be improved
 hist->SetMaximum(ymax+0.5); // maximum y-value - to be improved

  hist->GetXaxis()->SetRangeUser(-3,3);
  hist->GetXaxis()->SetNdivisions(510);
  hist->GetYaxis()->SetNdivisions(510);
  hist->GetXaxis()->SetTitle("#it{y_{#pi#pi}} [GeV]");
  hist->GetYaxis()->SetTitle(yTitle);
  hist->GetXaxis()->SetTitleOffset(1.1);
  hist->GetYaxis()->SetTitleOffset(1.1);
  hist->GetXaxis()->SetTitleSize(0.065);
  hist->GetYaxis()->SetTitleSize(0.065);
  hist->GetXaxis()->SetLabelSize(0.065);
  hist->GetYaxis()->SetLabelSize(0.065);


 hist->SetLineWidth(0);
 hist->SetLineColor(0);
 return hist;
 
} // end of TH1D* StyleHistoVSy()
  
// =====================================================================================









void SetFlowStyle()
{
 // Set style which will affect all plots.
 
 gStyle->Reset();

 gStyle->SetCanvasPreferGL(1); // enables transparency !!!

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



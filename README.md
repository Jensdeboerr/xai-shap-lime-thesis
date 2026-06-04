Bachelor thesis (Data Science & Society)

This repository goes with my BSc Data Science and Society thesis from the University of Groningen/Campus Fryslân (2025-2026). It has all the notebooks, processed data, and explanation outputs used to make the figures and tables for the thesis.

Structure: 

xai-shap-lime-thesis/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   ├── processed/          # model-ready data (committed)
│   │   ├── era5_supervised_preprocessed.zip   # engineered feature matrix (zipped)
│   │   ├── feature_columns.txt
│   │   ├── features_baseline.txt              # 15-feature instantaneous set
│   │   ├── features_selected_history.txt      # 19-feature operational set
│   │   └── features_full.txt                  # 92-feature full set
│   └── raw/                # NOT committed — see data/raw/README.md
├── notebooks/              # numbered pipeline, run in order
│   ├── 01_data_understanding_and_eda.ipynb
│   ├── 02_preprocessing_and_feature_engineering.ipynb
│   ├── 03_feature_set_definition.ipynb
│   ├── 04_modeling_xgboost.ipynb
│   ├── 05_shap_lime_analysis.ipynb
│   └── 06_consistency_analysis.ipynb
├── results/
│   ├── xgboost_model_comparison.csv           # metrics per feature configuration
│   ├── xgboost_validation_tuning_results.csv  # hyperparameter search results
│   ├── xgboost_best_features.csv              # features of the selected model
│   ├── xgboost_best_model_test_predictions.csv
│   ├── xai/                # SHAP + LIME explanation outputs
│   ├── consistency/        # agreement + stability metrics
│   └── models/             # trained model binaries (NOT committed)
├── figures/                # PNGs used in the thesis
└── scripts/                # helper/utility code



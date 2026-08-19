# Maps the EXACT class names from class_names.pkl to their knowledge_base filename.
# Use this for direct lookup when you already know the predicted condition
# (from the skin-classification model) — no need for embedding search in that case.
# Embedding/vector search (rag.py) is still useful for open-ended user questions
# that don't map 1:1 to a single condition.

CONDITION_TO_FILE = {
    "Light Diseases and Disorders of Pigmentation": "pigmentation.txt",
    "Lupus and other Connective Tissue diseases": "lupus_connective_tissue.txt",
    "Acne and Rosacea Photos": "acne_rosacea.txt",
    "Systemic Disease": "systemic_disease.txt",
    "Poison Ivy Photos and other Contact Dermatitis": "contact_dermatitis.txt",
    "Vascular Tumors": "vascular_tumors.txt",
    "Urticaria Hives": "hives_urticaria.txt",
    "Atopic Dermatitis Photos": "atopic_dermatitis.txt",
    "Bullous Disease Photos": "bullous_disease.txt",
    "Hair Loss Photos Alopecia and other Hair Diseases": "hair_loss_alopecia.txt",
    "Tinea Ringworm Candidiasis and other Fungal Infections": "fungal_infections.txt",
    "Psoriasis pictures Lichen Planus and related diseases": "psoriasis_lichen_planus.txt",
    "Melanoma Skin Cancer Nevi and Moles": "melanoma_skin_cancer.txt",
    "Nail Fungus and other Nail Disease": "nail_disease.txt",
    "Scabies Lyme Disease and other Infestations and Bites": "infestations_bites.txt",
    "Eczema Photos": "eczema.txt",
    "Exanthems and Drug Eruptions": "exanthems_drug_eruptions.txt",
    "Herpes HPV and other STDs Photos": "std_skin.txt",
    "Seborrheic Keratoses and other Benign Tumors": "benign_tumors.txt",
    "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions": "malignant_lesions.txt",
    "Vasculitis Photos": "vasculitis.txt",
    "Cellulitis Impetigo and other Bacterial Infections": "bacterial_infections.txt",
    "Warts Molluscum and other Viral Infections": "viral_infections.txt",
}

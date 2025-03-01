terraform {
  required_providers {
    okta = {
      source = "okta/okta"
      version = "~> 4.14.0"
    }
  }
}

provider "okta" {
    # DEV-123456
    org_name    = OKTA_ORG_NAME
    api_token   = OKTA_API_TOKEN
}

resource "okta_app_saml" "Test SAML App" {
  label                    = "example"
  sso_url                  = "https://example.com"
  recipient                = "https://example.com"
  destination              = "https://example.com"
  audience                 = "https://example.com/audience"
  subject_name_id_template = "$${user.userName}"
  subject_name_id_format   = "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
  response_signed          = true
  signature_algorithm      = "RSA_SHA256"
  digest_algorithm         = "SHA256"
  honor_force_authn        = false
  authn_context_class_ref  = "urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport"
}
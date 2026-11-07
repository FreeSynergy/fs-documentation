# Axelor - Description

## What the program does

Axelor is "ERP from one piece + process workshop": the modules are finished, but almost everything on top of them (fields, forms, approval workflows) is created in the App Builder/BPM designer. Anyone who wants to model processes without programming finds a consistent Java system here.

## Advantages

- **BPM tightly integrated** (approvals, task lists, SLA handling)
- AGPL, one stack (backend/frontend/builder)
- REST automatic — little integration work

## Differentiation

| System | Difference |
|--------|-------------|
| **Odoo** | Store ecosystem + website; Axelor process builder |
| **ERPNext** | Frappe/Python; Axelor Java/jBPM |
| **Bonita/BPM suites** | pure process engine; Axelor brings the ERP along as well |

## Technical details

- **Stack**: Java (Spring Boot base), jAvancé framework, PostgreSQL
- **Auth**: username+password, LDAP/SSO (check version); API: Basic/JWT token (`JSESSION`-less REST clients)
- **Deploy**: Docker, Tomcat WAR, Axelor Cloud
- **Licence**: AGPL (Open Suite), store modules partly commercial

## For whom it is suitable

- Medium-sized businesses with strong process/approval needs
- FreeSynergy skins: BPM node + REST model as a process skin template

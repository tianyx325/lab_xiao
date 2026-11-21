module github.com/lab-xiao/lab-xiao

go 1.19

require (
	github.com/HugoBlox/kit/modules/integrations/netlify v0.0.0-20260327032542-ef8ed449c7e8
	github.com/HugoBlox/kit/modules/blox v0.0.0-20260527025321-61f41d3667f1
	github.com/HugoBlox/kit/modules/slides v0.0.0-20260330182742-6a2f1ba2aeb5
)

replace github.com/HugoBlox/kit/modules/blox => ../kit-main/modules/blox
replace github.com/HugoBlox/kit/modules/analytics => ../kit-main/modules/analytics
replace github.com/HugoBlox/kit/modules/integrations/netlify => ../kit-main/modules/integrations/netlify
replace github.com/HugoBlox/kit/modules/slides => ../kit-main/modules/slides


variable "orx_file" {
  default = "../views/dev/employee_view.orx"
}

variable "env_file" {
  default = "../env/dev.env"
}

resource "null_resource" "radiantlogic_view" {
  provisioner "local-exec" {
    command = "python3 ../scripts/main.py deploy ${var.orx_file} ${var.env_file}"
  }

  triggers = {
    orx_hash = filesha256(var.orx_file)
  }
}

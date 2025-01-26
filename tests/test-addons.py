from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_opentelemetry_operator(self):
        """
        Sets up and validates OpenTelemetry Operator.
        """
        print("Enabling opentelemetry-operator")
        microk8s_enable("opentelemetry-operator")
        print("Validating opentelemetry-operator")
        self.validate_opentelemetry_operator()
        print("Disabling opentelemetry-operator")
        microk8s_disable("opentelemetry-operator")

    def validate_opentelemetry_operator(self):
        """
        Validate OpenTelemetry Operator.
        """

        wait_for_pod_state(
            "",
            "opentelemetry-operator",
            "running",
            label="app.kubernetes.io/component=controller-manager",
        )

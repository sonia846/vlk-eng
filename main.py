import os
from core.engine import ValkyrieEngine
from modules.scanner import ComplianceScanner
from utils.reporter import ReportGenerator

def main():
    print("==============================================")
    print("     VALKYRIE MULTI-MODULE SIMULATION SUITE   ")
    print("==============================================")
    
    # Initialize Core Architecture
    engine = ValkyrieEngine()
    audit_results = engine.run_security_audit()
    
    # Execute Scanner Sub-component
    scanner = ComplianceScanner(target_env=engine.config.get("lab_environment", "Local-Lab"))
    logs = scanner.scan_local_registry()
    
    # Trigger Multi-format Reporting Pipeline
    reporter = ReportGenerator()
    reporter.export_telemetry(audit_results, format_type="json")
    
    print("[SUCCESS] Full infrastructure stack evaluation completed successfully.")

if __name__ == "__main__":
    main()

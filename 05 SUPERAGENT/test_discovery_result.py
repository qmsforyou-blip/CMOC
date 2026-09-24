from discovery_result import build_discovery_result


def make_results():
    types = [
        "EXTRACTION_RECORDS",
        "DISTINCTION_RECORDS",
        "FORMULATION_RECORDS",
        "NOMENCLATURE_CANDIDATES",
        "CLASSIFICATION_RECORDS",
        "PASSPORT_RECORDS",
        "RELATION_CANDIDATES",
        "DECISION_RECORDS",
    ]
    tasks = [f"M{i:02d}" for i in range(1, 9)]
    return [
        {
            "status": "ACCEPT",
            "type": typ,
            "batch_id": f"BATCH-SRC-003-{task}-{i:03d}",
            "ref": f"BATCH-SRC-003-{task}-{i:03d}:OUTPUT",
            "records": [{"id": str(i)}],
        }
        for i, (task, typ) in enumerate(zip(tasks, types), 1)
    ]


def test_full_result():
    result = build_discovery_result(
        run_id="RUN-SRC-003-AUTOMATED-M01-M08-001",
        source={
            "source_id": "SRC-003",
            "package_id": "SOURCE-003-PACKAGE-001-CONTROLLED-5-6",
        },
        results=make_results(),
    )["discovery_result"]

    assert result["discovery_id"].startswith(
        "DISCOVERY-RESULT-SRC-003-"
    )
    assert list(result["outputs"]) == [f"M{i:02d}" for i in range(1, 9)]
    assert result["outputs"]["M08"]["batch_id"].endswith("M08-008")
    assert result["boundary"] == {
        "origin": "SOURCE_BOUND",
        "reconciliation": "NOT_PERFORMED",
    }
    assert all("records" not in item for item in result["outputs"].values())


def test_incomplete_rejected():
    try:
        build_discovery_result(
            run_id="R",
            source={"source_id": "S", "package_id": "P"},
            results=make_results()[:-1],
        )
    except ValueError as exc:
        assert "all 8" in str(exc)
    else:
        raise AssertionError("incomplete Discovery must be rejected")


def test_non_accept_rejected():
    results = make_results()
    results[6]["status"] = "REJECT"

    try:
        build_discovery_result(
            run_id="R",
            source={"source_id": "S", "package_id": "P"},
            results=results,
        )
    except ValueError as exc:
        assert "M07" in str(exc)
    else:
        raise AssertionError("non-ACCEPT Discovery stage must be rejected")
